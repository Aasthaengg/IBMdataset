N,M,X = map(int,input().split())
CA = [list(map(int,input().split())) for _ in range(N)]
ans = 10**9

for i in range(2**N):
  cost = 0
  skill = [0]*M
  cnt = 0
  for j in range(N):
    if (i>>j)&1 == 1:
      for k in range(M):
        skill[k] += CA[j][k+1]
      cost += CA[j][0]
  for l in range(M):
    if skill[l] >= X:
      cnt += 1
    if cnt == M:
      ans = min(ans,cost)
if ans == 10**9:
  print(-1)
else:
  print(ans)