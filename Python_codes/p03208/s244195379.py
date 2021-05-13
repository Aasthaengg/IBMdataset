N, K = map(int, input().split())
H = sorted([int(input()) for i in range(N)])

ans = float("inf")
for i in range(N-K+1):
    ans = min(ans, H[i+K-1]-H[i])

print(ans)