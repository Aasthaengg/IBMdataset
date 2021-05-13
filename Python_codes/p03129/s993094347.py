import math
N, K = map(int, input().split())
ans = 'YES'
if math.ceil(N / 2) < K:
  ans = 'NO'
print(ans)