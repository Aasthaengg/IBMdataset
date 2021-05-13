N, M = map(int, input().split())
ans = 0

if 2 * N == M:
    ans = N
elif 2 * N > M:
    ans = M // 2
else:
    ans += N
    M -= 2*N
    ans += M // 4

print(ans)