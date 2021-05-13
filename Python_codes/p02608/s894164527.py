from math import sqrt, ceil

N = int(input())

result = [0] * (N + 1)
t = ceil(sqrt(N))
for x in range(1, t + 1):
    for y in range(1, t + 1):
        for z in range(1, t + 1):
            n = x * x + y * y + z * z + x * y + y * z + z * x
            if n > N:
                break
            result[n] += 1

print(*result[1:], sep='\n')
