n, k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort(key=abs, reverse=1)

mod = 10**9+7
ans = 1
sign = 1
for i in range(k):
    ans *= a[i]
    ans %= mod
    if a[i] < 0:
        sign *= -1
    elif a[i] == 0:
        sign = 0
if sign >= 0:
    print(ans)
else:
    t = None
    ok = True
    for i in reversed(range(k)):
        if a[i] < 0:
            break
    else:
        ok = False
    for j in range(k, n):
        if a[j] > 0:
            break
    else:
        ok = False

    if ok:
        t = (a[i], a[j])

    ok = True
    for i in reversed(range(k)):
        if a[i] > 0:
            break
    else:
        ok = False
    for j in range(k, n):
        if a[j] < 0:
            break
    else:
        ok = False

    if ok:
        if t is None:
            t = (a[i], a[j])
        else:
            if (t[1]*a[i] - t[0]*a[j]) * t[0]*a[j] < 0:
                t = (a[i], a[j])

    if t is None:
        ans = 1
        a.reverse()
        for i in range(k):
            ans *= a[i]
            ans %= mod
        print(ans)
    else:
        print(ans*t[1] * pow(t[0], mod-2, mod) % mod)
