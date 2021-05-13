H, W, D = map(int, input().split())
number = [[0,0] for _ in range(H*W)]
cost = [0] * (H*W)
for i in range(H):
  a = list(map(int, input().split()))
  for j in range(W):
    number[a[j]-1] = [i, j]
for i in range(D):
  cost[i] = 0
for j in range(D, H*W):
  cost[j] = cost[j-D] + abs(number[j][0]-number[j-D][0]) + abs(number[j][1]-number[j-D][1])
Q = int(input())
for i in range(Q):
  L, R = map(int, input().split())
  print(cost[R-1] - cost[L-1])