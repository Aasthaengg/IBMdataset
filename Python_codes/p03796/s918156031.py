n = int(input())
dv = 10 ** 9 + 7
power = 1
for i in range(1, n + 1):
  power = (power * i) % dv
print(power)