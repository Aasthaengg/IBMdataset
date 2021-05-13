N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
ans = 10**10

for i in range(N - K + 1):
    ans_ = h[i + K - 1] - h[i]
    ans = min(ans, ans_)

print(ans)