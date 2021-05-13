import math
N = int(input())

ans = math.inf
y = int(math.sqrt(N))

for i in range(1, y+1):
    if N % i == 0:
        ans = min(ans, (i + int(N / i)) - 2)

print(ans)