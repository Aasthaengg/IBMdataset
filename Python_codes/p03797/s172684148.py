N, M = map(int, input().split())
ans = 0
# ans += min(N, M//2)
if min(N, M//2) == N:
    M -= N*2
    ans += N
    ans += M//4
else:
    ans += min(N, M//2)

print(ans)