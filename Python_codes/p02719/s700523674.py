N, K = map(int, input().split())

if N == 0 or K == 1:
    N = 0
elif N == K:
    N = 0
elif N % K == 0:
    N = 0
else:
    N = N % K
    while N != 0:
        m = abs(N - K)
        if N < m:
            break
        else:
            N = m

print(N)