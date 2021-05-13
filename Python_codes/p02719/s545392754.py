N, K = map(int,input().split())

if N > K:
  N = N % K

min_N = float("inf")
while min_N != N:
  min_N = min(N,min_N)
  if N == K or N == 0 or K == 0:
    print(0)
    exit(0)
  
  N = abs(N - K)
  
print(min_N)