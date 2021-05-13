N = int(input())
S = input()
X = list(int(x) for x in S)


def popcount(x):
    return bin(x).count("1")


def f(x):
    if x == 0:
        return 0
    return f(x % popcount(x)) + 1


MAX = 2 * 10 ** 5 + 5
# print(X)

pc = sum(X)  # もとのpopcount

ans = [0] * (N + 1)
for b in range(2):
    npc = pc  # 今のpopcount
    if b == 0:
        npc += 1
    else:
        npc -= 1
    if npc <= 0:
        continue
    # もとの割った余りを求めていく
    r0 = 0
    for i in range(N):
        r0 = (r0 * 2) % npc
        r0 += X[i]
    k = 1
    for i in reversed(range(N)):
        if X[i] == b:  # i桁目がbのものだけ処理する。
            r = r0  # 今の桁を変えたときに割った余りがどう変化するか
            if b == 0:
                r = (r + k) % npc
            else:
                r = (r - k + npc) % npc
            # i桁目をフリップしたときの値がここまでで求まった。
            ans[i] = f(r) + 1
        k = (k * 2) % npc

for i in range(N):
    print(ans[i])
