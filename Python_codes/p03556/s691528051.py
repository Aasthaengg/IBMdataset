# ABC 077: B – Around Square
n = int(input())
result = 1

for i in range(int(n ** (1 / 2) + 1)):
    result = max(result, i * i)

print(result)