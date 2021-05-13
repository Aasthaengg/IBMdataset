N = int(input())
power = 1
K = 10 ** 9 + 7
for n in range(N):
  power *= (n + 1)
  if power >= K:
    power %= K
print(power)