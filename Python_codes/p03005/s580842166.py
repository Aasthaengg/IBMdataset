N, K = map(int, input().split())
if K == 1:
    print(0)
elif N > K:
    print(N - K)
elif N == K:
    print(0)
else:
    print(1)