N, M = map(int, input().split())

ans = 0

ans += min(N, M//2)

N -= ans
M -= ans * 2

ans += M // 4

print(ans)
