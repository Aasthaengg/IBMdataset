n, k = map(int, input().split())
k -= 1

x = list(map(int, input().split()))

ans = float("inf")
for i in range(n):
    if i + k >= n:
        continue
    d = abs(x[i] - x[i + k]) + min(abs(x[i]), abs(x[i + k]))
    ans = min(ans, d)

print(ans)