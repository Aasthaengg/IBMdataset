N, M = map(int, input().split())


if N == 1 and M == 1:
    ans = 1
elif N <= 2 and M <= 2:
    ans = 0
elif N == 1 or M == 1:
    ans = max(N, M) - 2
else:
    ans = N * M - (2 * N + 2 * M - 4)

print(ans)
