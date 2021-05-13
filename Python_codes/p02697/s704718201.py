N, M = map(int, input().split())

A = list(range(M))
B = list(range(M, 2*M))[::-1]
B = [-2-i for i in range(M//2)] + B[M//2:]

for a, b in zip(A, B):
    print(a % N + 1, b % N + 1)
