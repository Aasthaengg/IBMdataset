n, m=map(int, input().split())
D=[[] for i in range(n)]

for i in range(m):
    p, y=map(int, input().split())
    D[p-1].append((y, i))

ans=[0]*m

for i, d in enumerate(D):
    d.sort()
    for k, (y, j) in enumerate(d):
        ans[j]=str(i+1).zfill(6) + str(k+1).zfill(6)

print(*ans, sep='\n')