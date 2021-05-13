n,k = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
l.sort()
a,b = [list(i) for i in zip(*l)]
p = 0
for i in range(n):
    p += b[i]
    if p >= k:
        print(a[i])
        break