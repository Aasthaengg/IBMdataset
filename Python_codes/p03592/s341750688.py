N, M, K = map(int, input().split())

for n in range(N + 1):
    for m in range(M + 1):
        tmp = m * (N - n) + n * (M - m)
        if tmp == K:
            print ('Yes')
            exit()

print ('No')