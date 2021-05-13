import math

N = int(input())

result = 0
n = math.sqrt(N)
n = math.ceil(n)

for i in range(1, n + 1):
    for j in range(i, N // i + 1):
        if i * j < N:
            if i == j:
                result += 1
            else:
                result += 2
        else:
            break
print(result)