n, x, y = map(int, input().split())

ans = {i:0 for i in range(1, n)}

for i in range(1, n):
    for j in range(i + 1, n + 1):
        d = min(j - i, abs(i - x) + 1 + abs(j - y))
        ans[d] += 1

for k in range(1, n):
    print(ans[k])