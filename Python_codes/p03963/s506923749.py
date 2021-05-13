def countpattern(N, K) :
  pattern = K
  for i in range(1, N) : 
    pattern *= K - 1
    
  return pattern

N, K = tuple(map(int, input().split()))

print(countpattern(N, K))