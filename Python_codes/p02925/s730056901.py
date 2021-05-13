n = int(input())
g = [[-1, -1] for i in range(n*n)]
z = [0] * (n*n)

a = []
for _ in range(n):
    a.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(n-2):
        p, q = (i, a[i][j]-1)
        r, s = (i, a[i][j+1]-1)
        r, s = (min(r, s), max(r ,s))
        if p < q:
            g[p*n+q][0] = r*n + s
        else:
            g[q*n+p][1] = r*n + s
        z[r*n+s] += 1

qu = set([])
for i in range(n):
    p, q = (i, a[i][0]-1)
    p, q = (min(p, q), max(p ,q))
    if z[p*n+q] == 0:
        qu.add(p*n+q)

ans = 0
re = 0
while True:
    nqu = []
    while qu:
        s = qu.pop()
        re += 1
        for t in g[s]:
            if t != -1:
                z[t] -= 1
                if z[t] == 0:
                    nqu.append(t)
    ans += 1    
    qu = nqu
    if not qu:
        break

if re == n*(n-1)//2:
    print(ans)
else:
    print(-1)