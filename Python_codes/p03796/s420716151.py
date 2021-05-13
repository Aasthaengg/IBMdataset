mod = 10 ** 9 + 7
n = 1
for i in range((int)(input()), 0, -1):
  n *= i
  n %= mod
print(n)