N = int(input())
ans = 10 ** 12
for x1 in range(1, int(N ** 0.5) + 1):
    if N % x1 == 0:
        y1 = N // x1
        now = x1 + y1 - 2
        ans = min(ans, now)
print(ans)