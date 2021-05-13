n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()
ans = max(h)
for i in range(0, n - k + 1):
    h_diff = h[i + k - 1] - h[i]
    ans = min(ans, h_diff)
print(ans)
