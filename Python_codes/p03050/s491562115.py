from math import floor

N = int(input())

ans = 0
for i in range(1, floor(N ** 0.5) + 1):
    q = N // i
    if not N % i and i + 2 <= q:
        ans += q - 1
print(ans)
