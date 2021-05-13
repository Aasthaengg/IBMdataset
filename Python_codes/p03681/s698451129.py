import math
N, M = map(int, input().split())

if N == M:
  ans = math.factorial(N) % (10**9+7)
  ans = (ans**2) % (10**9+7)
  ans = (ans*2) % (10**9+7)
elif N - M == 1:
  ans = math.factorial(M) % (10**9+7)
  ans = (ans**2) % (10**9+7)
  ans = (ans*N) % (10**9+7)
elif M - N == 1:
  ans = math.factorial(N) % (10**9+7)
  ans = (ans**2) % (10**9+7)
  ans = (ans*M) % (10**9+7)
else:
  ans = 0
  
print(ans)