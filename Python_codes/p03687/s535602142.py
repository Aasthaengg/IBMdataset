s = list(input())
ans = 100
n = len(s)
q = list(set(s))
for _ in q:
    x = _
    m = n - 1
    t = list(s)
    r = ['0'] * m
    while len(set(t)) > 1:
        for i in range(m):
            if t[i] == x or t[i+1] == x:
                r[i] = x
            else:
                r[i] = t[i]
        m -= 1
        t = list(r)
        r = ['0'] * m
    ans = min(ans,n-len(t))
print(ans)