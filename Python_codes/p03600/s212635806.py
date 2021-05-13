import sys
readline = sys.stdin.readline

N = int(readline())

A = [None] * N
for i in range(N):
  A[i] = list(map(int,readline().split()))
  
# まずワーシャルフロイド表を作る
# ワーシャルフロイド表より大きな数値が元の表にあったら、最短距離の表ではないので-1
# 最短距離の表になっているのであれば、
# A[1][3]に行くときにA[1][2] + A[2][3]となるのであれば、
# A[1][3]のほうだけansに記録していく

import copy
newA = copy.deepcopy(A)

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == k or k == j or i == j:
        continue
      if A[i][k] + A[k][j] < A[i][j]:
        print(-1)
        exit(0)
      elif A[i][k] + A[k][j] == A[i][j]:
        # A[i][j]の道路は不要
        newA[i][j] = 0

ans = 0
for a in newA:
  ans += sum(a)
print(ans // 2)