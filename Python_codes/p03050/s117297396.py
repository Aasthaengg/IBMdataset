from math import sqrt
N = int(input())
ans = 0
# if N // i = p, N % i = p, 
# N = pi + p = p(i+1)
# p < sqrt(N) and p < i 
for p in range(1,N):
  if p > N/p - 1:
    break
  if N % p > 0:
    continue
  i = N//p - 1
  if p >= i:
    break
  ans += i
    
print(ans)