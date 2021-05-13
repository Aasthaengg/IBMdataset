N,M = map(int,input().split())
ans = 1
if abs(N-M) >= 2:
  print(0)
elif abs(N-M) == 1:
  for i in range(1,min(N,M)+1):
    ans *= i
    ans = ans % (10**9 + 7)
  ans = ans**2 * max(N,M)
  ans = ans % (10**9 + 7)
  print(ans)
elif abs(N-M) == 0:
  for i in range(1,N+1):
    ans *= i
    ans = ans % (10**9 + 7)
  ans = ans**2
  ans *= 2
  ans = ans % (10**9 + 7)
  print(ans)