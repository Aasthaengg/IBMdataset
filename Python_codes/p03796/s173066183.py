N = int(input())
power = 1

for i in range(1, N+1):
  power *= i
  if power < 10**9 + 7:
    continue
  power = power % (10**9 + 7)

print(power)