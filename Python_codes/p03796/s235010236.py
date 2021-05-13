N = int(input())
ans = 1
for i in range(2, N+1):
  ans *= i % 1000000007
  ans = ans % 1000000007
print(ans % 1000000007)