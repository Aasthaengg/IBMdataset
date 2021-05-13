N, K = map(int, input().split())
howmany = K * (K - 1) ** (N - 1)
if K < 2**31:
    print(howmany)
else:
    pass
