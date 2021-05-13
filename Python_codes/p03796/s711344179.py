N = int(input())
mod = 10 ** 9 + 7

power = 1
for i in range(1, N + 1):
    power = power * i % mod

print(power)