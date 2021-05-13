[n,m] = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
        print(str(a[i][j]) + " ",end='')
    print(s)

t = []
for j in range(m):
    u = 0
    for i in range(n):
        u += a[i][j]
    t.append(u)

for j in range(m):
    print(str(t[j]) + " ",end='')
print(sum(t))