N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()
ans = 11**9
for i in range(N - K + 1):
    min_tree = h[i]
    max_tree = h[i + K - 1]
    ans = min(ans, max_tree - min_tree)
print(ans)
