n = int(input())

power = 1
for i in range(n):
    power = power * (i+1)
    if power > 1000000007:
        power = power % 1000000007

print(power)