import math
N, K = map(int, input().split())
for i in range(1, K+1):
  ans = 0
  blue = math.factorial(K-1) // (math.factorial(i-1)*math.factorial(K-i))
  if N-K+1-i < 0:
    red = 0
  else:
    red = math.factorial(N-K+1) // (math.factorial(i)*math.factorial(N-K+1-i))
  ans = blue * red
  ans = ans % (10**9+7)
  print(int(ans))