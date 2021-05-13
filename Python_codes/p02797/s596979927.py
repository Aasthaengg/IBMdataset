N, K, S = map(int, input().split())

A = [None] * N
for i in range(N):
    if i < K:
        A[i] = S
    else:
        A[i] = (S + 1) % (10 ** 9)

print(' '.join(map(str, A)))