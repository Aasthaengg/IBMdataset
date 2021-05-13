N, K = map(int, input().split())

if N < K:
    print(1)
elif N == K or K == 1:
    print(0)
else:
    print(N - K)