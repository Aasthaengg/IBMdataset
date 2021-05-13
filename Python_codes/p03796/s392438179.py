n = int(input())

power = 1

for a in range(1, n+1):
    power *= a
    power %= (10**9+7)

print(power)
