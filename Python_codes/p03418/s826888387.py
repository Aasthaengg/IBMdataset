N, K = map(int, input().split())
res = 0
if K == 0:
    print(N*N)
else:
    for i in range(K+1, N+1):
        res += (i-K) * int(N/i)
        if N % i - K >= 0:
            res += (1 + N % i - K)
    print(res)