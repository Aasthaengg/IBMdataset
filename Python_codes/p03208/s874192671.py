N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()
ans = max(h)
for i in range(N-K+1):
    if h[i+K-1]-h[i] < ans:
        ans = h[i+K-1]-h[i]
print(ans)
