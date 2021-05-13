N, K = map(int, input().split())
h = sorted([int(input()) for i in range(N)])

hmax = 0
hmin = 0
ans = 10**10
for i in range(N - K + 1):
    hmax = h[i + K - 1]
    hmin = h[i]
    if hmax - hmin < ans:
        ans = hmax - hmin
print(ans)
