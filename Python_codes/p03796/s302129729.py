n = int(input())
power = 1
mod = 10**9 + 7
for i in range(n):
    power = power * (i+1)
    power %= mod
print(power)
