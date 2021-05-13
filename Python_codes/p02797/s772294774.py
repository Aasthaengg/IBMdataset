N, K, S = map(int, input().split())

ans = [S]*K

if S == 1:
    ans += ([2]*(N-K))
else:
    ans += ([S-1]*(N-K))

print(*ans, sep=' ')