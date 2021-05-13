n,m = map(int,input().split())
l = [list(map(int,input().split())) for i in range(m)]
a,b = [list(i) for i in zip(*l)]

for i in range(1,n+1):
    t = 0
    t += a.count(i)
    t += b.count(i)
    print(t)