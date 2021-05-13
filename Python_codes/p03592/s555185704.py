N, M, K = map(int, input().split())

for n in range(N + 1):
    if (N - 2 * n) == 0:
        continue
    if (K - n * M) % (N - 2 * n) == 0:
        if 0 <= (K - n * M) // (N - 2 * n) <= M:
            print ('Yes')
            exit()

print ('No')