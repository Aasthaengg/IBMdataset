N, K = map(int, input().split())
A = K
if N != 1:
    for i in range(N - 1):
        A *= (K - 1)
print(A)