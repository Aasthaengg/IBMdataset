
N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ctr = [0, 0, 0]
ans = 1
for a in X:
    ptn = sum(a == v for v in ctr)
    ans = ans * ptn % MOD

    if ans == 0:
        break

    for i in range(3):
        if ctr[i] == a:
            ctr[i] += 1
            break

print(ans)
