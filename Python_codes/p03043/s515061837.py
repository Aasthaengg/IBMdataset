import math
n, k = map(int, input().split())
ans = 0.0
if n >= k:
  ans += (n-k+1)/n
  
for i in range(1, min(n+1, k)):
  now = i
  p = 1/n
  while(now <k):
    now *= 2
    p /= 2
  ans += p
  
print(ans)