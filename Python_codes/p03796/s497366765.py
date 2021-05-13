N = int(input())
power = 1
for n in range(1, N+1):
    power = power % (10**9+7) * n
print(power % (10**9+7))
