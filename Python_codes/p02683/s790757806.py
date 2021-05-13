n,m,l = map(int,input().split())
c = [list(map(int,input().split())) for i in range(n)]
p = 'a'
for i in range(2**n):
    x = i
    y = [0] * m
    z = 0
    for j in range(n):
        if x % 2 != 0:
            z += c[j][0]
            for k in range(m):
                y[k] += c[j][k+1]
        x = x // 2
    if min(y) >= l:
        if p != 'a':
            p = min(p,z)
        else:
            p = z
if p != 'a':
    print(p)
else:
    print(-1)