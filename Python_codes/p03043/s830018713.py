import math
N, K = map(int, input().split())
p = 0
for i in range(1,N+1):
  if i < K:
    times = math.ceil(math.log2(K/i))
    p = p + (1/N)*(1/2)**times
  else:
    p = p + (1/N)
print(p)
  
