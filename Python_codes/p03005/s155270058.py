
S = list(map(int, input().split()))

N = S[0]
K = S[1]


if N % K == 0:
    print(0)
else:
    print(N-K)
