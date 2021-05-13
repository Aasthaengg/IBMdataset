from math import ceil

N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
    print(1)
    exit()


print(ceil((N - K) / (K - 1)) + 1)
