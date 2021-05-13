def solve():
  ans = 0
  H, W = map(int, input().split())
  S = [0]*(H+2)
  S[0] = '*'*(W+2)
  S[H+1] = '*'*(W+2)
  for h in range(1,H+1):
    S[h] = '*' + input() + '*'
  L = [[0]*(W+2) for _ in range(H+2)]
  R = [[0]*(W+2) for _ in range(H+2)]
  U = [[0]*(W+2) for _ in range(H+2)]
  D = [[0]*(W+2) for _ in range(H+2)]
  for h in range(1,H+2):
    for w in range(1,W+2):
      if S[h][w]=='.':
        if S[h][w-1]=='.':
          L[h][w] = L[h][w-1]+1
        if S[h-1][w]=='.':
          U[h][w] = U[h-1][w]+1
  for h in range(H+1,0,-1):
    for w in range(W+1,0,-1):
      if S[h][w]=='.':
        if S[h][w+1]=='.':
          R[h][w] = R[h][w+1]+1
        if S[h+1][w]=='.':
          D[h][w] = D[h+1][w]+1
  total = [[0]*(W+2) for _ in range(H+2)]
  for h in range(1,H+2):
    for w in range(1,W+2):
      if S[h][w]=='.':
        total[h][w] = L[h][w]+R[h][w]+U[h][w]+D[h][w]+1
        ans = max(ans,total[h][w])
  return ans
print(solve())