s = 0
N, K = map(int, input().split())
if K == 0:
  print(N*N)
else:
  for b in range(K+1, N+1):
    q = N//b
    r = N%b
    s += q*(b-K)
    if r >= K:
      s += r-K+1
  print(s)