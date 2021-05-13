import math

N = int(input())
ans = 0
for i in range(1, int(math.sqrt(N) + 2)):
    if N % i:
        continue
    m = N // i - 1
    if m <= 0:
        continue
    if N // m < m:
        ans += m
print(ans)
