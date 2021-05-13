n = int(input())
a = list(map(int,input().split()))
l = {}
r = {}
for i in range(n):
    p = i+a[i]
    q = i-a[i]
    if p < n:
        if p in l:
            l[p] = l[p]+1
        else:
            l[p] = 1
    if q > 0:
        if q in r:
            r[q] = r[q]+1
        else:
            r[q] = 1
ans = 0
for i in l:
    if i in r:
        ans+= l[i]*r[i]
print(ans)
