N = int(input())

ans = 1

for i in range(N):
  ans *= i + 1
  if ans > 1000000007:
    ans = ans % 1000000007

print(ans)