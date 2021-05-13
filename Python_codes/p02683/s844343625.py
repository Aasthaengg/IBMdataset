N, M, X = map(int, input().split())
C = [(list(map(int, input().split()))) for _ in range(N)]
 
# bit全探索を行い、参考書に関する全ての組みについて、値段と理解度を求める
ans = 10**10
for i in range(2**N):
  U = [0]*(M+1)
  for j in range(N):
    if ((i >> j) & 1):
      for k in range(M+1):
        U[k] += C[j][k]
  
  # ある組みが条件を満たし、その値段が現時点で最小なら、更新する
  if sum([u >= X for u in U[1:]]) == M:
    ans = min(ans, U[0])

if ans == 10**10: print(-1)
else: print(ans)