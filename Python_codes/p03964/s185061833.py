N = int(input())
TA = [[int(i) for i in input().split()] for _ in range(N)]
ans = [i for i in TA[0]]
for ta in TA[1:]:
    t, a = ta
    if t == a == 1:
        m = max(ans)
        ans = [m, m]
        continue
    si = 0
    sn = t
    ln = a
    if t > a:
        si = 1
        sn = a
        ln = t
    if ans[si] % sn:
        ans[si] = ans[si] // sn * sn + sn
    n = ans[si] // sn * ln
    if ans[si ^ 1] <= n:
        ans[si ^ 1] = n
    else:
        if ans[si ^ 1] % ln:
            ans[si ^ 1] = ans[si ^ 1] // ln * ln + ln
        ans[si] = ans[si ^ 1] // ln * sn
print(sum(ans))