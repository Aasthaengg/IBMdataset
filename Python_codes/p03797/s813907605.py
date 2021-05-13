N, M = map(int, input().split())

if N * 2 > M:
    print(M // 2)
    exit()

ans = N
ans += (M - 2 * N) // 4
print(ans)
