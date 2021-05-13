from numba import jit


@jit
def solve(N, K, A):
    for _ in range(K):
        imos = [0] * (N+1)
        for i in range(N):
            left = max(0, i-A[i])
            right = min(N-1, i+A[i])+1
            imos[left] += 1
            imos[right] += -1

        next_A = [0] * N
        next_A[0] = imos[0]
        for i in range(1, N):
            next_A[i] = next_A[i-1] + imos[i]

        if A == next_A:
            return A
        A = next_A
    return A


N, K = map(int, input().split())
A = [int(x) for x in input().split()]
print(" ".join([str(x) for x in solve(N, K, A)]))
