N = int(input())

power = 1
for i in range(1, N + 1):
    power = power * i
    if power > 1000000000:
        power = power % 1000000007

print(power % 1000000007)
