import math
def digsum(A):
  n = math.floor(math.log10(A))
  tmp = 0
  for i in range(n,0,-1):
    tmp += A // (10**i)
    A = A % (10**i)
  return tmp + A
  
N = int(input())
ans = 10**9
for i in range(1,N//2+1):
  ans = min(ans, digsum(i) + digsum(N-i))
print(ans)