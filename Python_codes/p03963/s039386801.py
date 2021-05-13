N,K = list(map(int, input().split()))
k = K
if N >= 2:
    for i in range(N - 1):
        k = k *(K - 1)
print(k)