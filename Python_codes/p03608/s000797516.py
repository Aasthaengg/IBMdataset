N, M, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[float('inf')]*N for _ in range(N)]
for i in range(M): #ひとまず枝があるペアは枝の長さをセット
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

ans = float('inf')
for p in permutations(r,R):
  cnt = 0
  for i in range(1,R):
    cnt += d[p[i-1]-1][p[i]-1]
  ans = min(ans,cnt)
print(ans)