import math

N,M = map(int,input().split())

T = M * 1900 + (N-M) * 100

p = (1/2)**M
p2 = (1/2)**M
ans = 0
for i in range(1,500000):
  ans += T * p2 * i
  p2 = p2 * (1-p)
  
print(round(ans))
