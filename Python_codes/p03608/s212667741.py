from itertools import permutations

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,m,r= map(int,input().split())
moku = list(map(int,input().split()))
d = [[float("inf")]*n for i in range(n)] 

for i in range(m):
    x,y,z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
p = warshall_floyd(d)

a = [i for i in range(r)]
zyun = list(permutations(a))

ans = 10**9
for i in zyun:
    cou = 0
    for j in range(r-1):
        cou += p[moku[i[j]]-1][moku[i[j+1]]-1]
    ans = min(ans,cou)
print(ans)