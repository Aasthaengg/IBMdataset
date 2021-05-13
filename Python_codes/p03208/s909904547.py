N, K = map(int, input().split())
High = [int(input()) for _ in range(N)]
High.sort()
ans = float('inf')
for i in range(N - K + 1):
    ans = min(High[K + i - 1] - High[i], ans)

print(ans)
