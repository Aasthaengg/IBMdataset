import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

# 階層iが取り得る最小値と最大値を記録する
minV = [0 for i in range(N + 1)]
maxV = [0 for i in range(N + 1)]

minV[-1] = A[-1]
maxV[-1] = A[-1]
for i in range(len(A) - 2, -1, -1):
  leaf = A[i] # その階層に必要な葉の数
  minV[i] = (minV[i + 1] + 1) // 2 + leaf
  maxV[i] = maxV[i + 1] + leaf

if 1 < minV[0] or maxV[0] < 1:
  print(-1)
  exit(0)

# 最大頂点数を確定していく
V = [0] * (N + 1)
V[0] = 1
for i in range(1, N + 1):
  V[i] = min((V[i - 1] - A[i - 1]) * 2, maxV[i]) # 親の頂点数から葉の数を引いたものの2倍

print(sum(V))