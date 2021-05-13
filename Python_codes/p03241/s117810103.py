N, M = list(map(int, input().split()))

ans = 1
for x in range(1, 10 ** 5 + 10):
    if M % x == 0:
        if N * x <= M:
            ans = max(ans, x)
        if N * (M // x) <= M:
            ans = max(ans, M // x)

print(ans)
