H, W, K = map(int, input().split())
A = [[0]*W for i in range(H+1)]
A[0][0] = 1
MOD = 10**9+7
for i in range(H):
  for j in range(W):
    for k in range(1<<(W-1)):
      for l in range(W-1):
        if (k>>l)&1 and (k>>(l+1))&1:
          break
      else:
        if j>0 and (k>>(j-1))&1:
          A[i+1][j-1] += A[i][j]
          A[i+1][j-1] %= MOD
        elif j<W-1 and (k>>j)&1:
          A[i+1][j+1] += A[i][j]
          A[i+1][j+1] %= MOD
        else:
          A[i+1][j] += A[i][j]
          A[i+1][j] %= MOD

print(A[H][K-1])