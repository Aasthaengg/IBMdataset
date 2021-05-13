N = int(input())

MOD = 1000000007
power = 1
for i in range(1, N+1):
  power = power * i % MOD
print(power)