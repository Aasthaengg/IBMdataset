N, M, R = map(int, input().split())
r = list(map(int, input().split()))

#Warshall Floyd
d = [[float('inf')]*N for _ in range(N)]
for _ in range(M): #ひとまず枝があるペアは枝の長さをセット
    a,b,t = map(int, input().split())
    d[a-1][b-1] = t
    d[b-1][a-1] = t

for i in range(N):
    d[i][i] = 0 #自身への最短経路は0
#三重ループ
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

from itertools import groupby, accumulate, product, permutations, combinations
def solve(r,d):
    ans = float('inf')
    for p in permutations(r,R):
        dist = 0
        for i in range(R-1):
            dist += d[p[i]-1][p[i+1]-1]
        ans = min(ans,dist)
    return ans
print(solve(r,d))