import math

N, res = int(input()), 0
for i in range(1, int(math.sqrt(N) + 1)):
    if N >= i * (i + 1) + i and (N - i) % i == 0:
        res += (N - i) // i
print(res)
