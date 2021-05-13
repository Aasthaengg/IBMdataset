N, K = map(int, input().split())

if K == 0:
    print(N * N)
else:
    cnt = 0
    for b in range(1, N+1):
        l_max = N // b
        for l in range(l_max + 1):
            k = min(b-1, N - b*l)
            if k >= K:
                cnt += k - K + 1

    print(cnt)