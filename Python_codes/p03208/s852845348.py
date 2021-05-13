N, K = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))

h.sort()
ans = 10**10
for i in range(N-K+1):
    hmin = h[i]
    hmax = h[i+K-1]
    ans = min(ans, (hmax-hmin))
print(ans)