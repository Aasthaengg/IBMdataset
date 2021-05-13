import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
f = bisect.bisect_left(a,0)
res = []
if f == 0:
    t = a[0]
    for i in range(1,n-1):
        res.append([t,a[i]])
        t = t - a[i]
    res.append([a[n-1],t])
    t = a[n-1] - t
elif f == n:
    t = a[n-1]
    for i in range(n-1):
        res.append([t,a[i]])
        t = t - a[i]
else:
    t = a[f-1]
    for i in range(f+1,n):
        res.append([t,a[i]])
        t = t - a[i]
    res.append([a[f],t])
    t = a[f] - t
    for i in range(f-1):
        res.append([t,a[i]])
        t = t - a[i]
    

print(t)
for sres in res:
    print(" ".join(map(str, sres)))