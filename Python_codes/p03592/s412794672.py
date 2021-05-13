N, M, K = map(int, input().split())

ans = 0
for n in range(N + 1):
    for m in range(M + 1):
        black = n * (M - m) + m * (N - n)
        if black == K:
            print('Yes')
            exit()
print('No')
