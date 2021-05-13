n, k = list(int(x) for x in input().split())

ans = 0

for i in range(1, n + 1):
    x = i + (k - 1)
    if x <= n:
        ans += 1

print(ans)