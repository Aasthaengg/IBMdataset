N, M, K = map(int, input().split())

for n in range(N + 1):
    for m in range(M + 1):
        if n * M + m * N - n * m * 2 == K:
            print('Yes')
            exit()

print('No')