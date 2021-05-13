n,m = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
a,b = [list(i) for i in zip(*l)]
l = [list(map(int,input().split())) for i in range(m)]
c,d = [list(i) for i in zip(*l)]

for i in range(n):
    p = 10 ** 9
    t = 50
    for j in range(m):
        e = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if p > e:
            p = e
            t = j + 1
    print(t)