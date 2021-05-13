N, M, r = map(int, input().split())
R = list(map(lambda x:int(x)-1, input().split()))
d = [[1<<30]*N for _ in range(N)]
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
ans = 1<<30
for per in permutations(R,r):
  cnt = 0
  for i in range(r-1):
    cnt += d[per[i]][per[i+1]]
  ans = min(ans, cnt)
print(ans)