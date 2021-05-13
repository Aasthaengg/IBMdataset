d, g =map(int,input().split())
a = []
b = []
for i in range(d):
    p,c = map(int,input().split())
    a.append(p)
    b.append(c)
ans = float('inf')
for i in range(2**d):
    ten = 0
    mon = 0
    for j in range(d):
        if i>>j&1:
            ten += a[j]*((j+1)*100)+b[j]
            mon += a[j]
    if ten < g:
        for j in range(d):
            tenp = ten
            monp = mon
            if i>>j&1 == 0:
                for k in range(a[j]-1):
                    tenp += (j+1)*100
                    monp += 1
                    if tenp >= g:
                        ans = min(ans,monp)
    else:

        ans = min(ans,mon)
print(ans)