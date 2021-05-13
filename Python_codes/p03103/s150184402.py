n,m = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
l.sort()
a,b = [list(i) for i in zip(*l)]
j = 0
p = 0

while m > 0:
    if b[j] <= m:
        p += a[j] * b[j]
        m -= b[j]
        j += 1
    else:
        p += a[j] * m
        m = 0

print(p)