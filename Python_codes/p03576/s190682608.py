n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in [0] * n]
a = XY.sort()
ans = float("inf")
for i in range(n - k + 1):
    for j in range(i + k, 1 + n):
        x = XY[j - 1][0] - XY[i][0]
        now = XY[i:j]
        now.sort(key=lambda x: x[1])
        for w in range(j - i - k + 1):
            ans = min(ans, x * (now[w + k - 1][1] - now[w][1]))

print(ans)