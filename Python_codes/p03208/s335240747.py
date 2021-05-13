N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
ans = float('inf')
h.sort()
for i in range(N-K+1):
    if ans > h[i+K-1] - h[i]:
        ans = h[i+K-1] - h[i]
print(ans)