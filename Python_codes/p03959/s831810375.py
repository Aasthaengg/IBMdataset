n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

if max(t) != max(a):
    print(0)
    exit()


def f(li, rev):
    if rev:
        li = li[::-1]

    cnts = [0] * n
    cands = [0] * n
    mx = 0
    cnt = 0
    for i, e in enumerate(li):
        if e > mx:
            cnts[i] = 1
            cands[i] = e
            cnt = e
            mx = e
        else:
            cnts[i] = cnt

    if rev:
        cnts = cnts[::-1]
        cands = cands[::-1]

    return cnts, cands


t_cnt, t_cand = f(t, False)
a_cnt, a_cand = f(a, True)

for e1, e2 in zip(a, t_cand):
    if e2 > e1:
        print(0)
        exit()

ans = 1
for e1, e2 in zip(t_cnt, a_cnt):
    ans *= min(e1, e2)
    ans %= mod

print(ans)
