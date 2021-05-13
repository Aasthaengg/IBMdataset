from itertools import permutations
n,m,r=map(int, input().split())
r_l=[int(i)-1 for i in input().split()]
town = [[float("INF")]*n for _ in range(n)]
for i in range(m):
    a,b,c=map(int, input().split())
    town[a-1][b-1]=c
    town[b-1][a-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            town[i][j] = min(town[i][j],town[i][k]+town[k][j])
res = float("INF")
for root in list(permutations(r_l)):
    tmp = 0
    for i in range(1,r):
        tmp += town[root[i]][root[i-1]]
    res = min(tmp,res)

print(res)
