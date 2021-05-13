N = int(input())
max_power = 0
for a in range(1, N + 1):
    if a**2 <= N:
        max_power = a**2
    else:
        break
print(max_power)