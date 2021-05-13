N, M = map(int, input().split())

x = min(N, M//2)

ans = x + (M - 2 * x) // 4
print(ans)