N, M = map(int, input().split())

ans = 0
if N >= M // 2:
    ans += M // 2
    N -= M // 2
    M = 0
else:
    ans += N
    M -= 2 * N
    N = 0
    ans += M // 4

print(ans)
