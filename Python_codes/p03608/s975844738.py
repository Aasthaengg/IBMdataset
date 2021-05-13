import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,m,r = map(int,readline().split())

lst1 = [[float("inf")]*n for _ in range(n)]

lst2 = list(map(int,readline().split()))
for i in range(len(lst2)):
    lst2[i] -= 1

for i in range(m):
    x,y,w = map(int,readline().split())
    lst1[x-1][y-1] = w
    lst1[y-1][x-1] = w

def warshall_floyd(d): #隣接行列を入れる
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

lst1 = warshall_floyd(lst1)

ans = 10**10
for i in list(itertools.permutations(lst2)):
    res = 0
    before = i[0]
    for j in i[1:]:
        res += lst1[before][j]
        before = j

    ans = min(res,ans)
print(ans)