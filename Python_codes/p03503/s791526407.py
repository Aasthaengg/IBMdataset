from itertools import product
A = {}
B = {}
N = int(input())

for n in range(1, N + 1):
    A[n] = input().split()

for n in range(1, N + 1):
    B[n] = [int(m) for m in input().split()]


ans = -10**10

for C in product(('1', '0'), repeat=10):
    if C != tuple('0' * 10):
        D = {v: 0 for v in range(1, N + 1)}
        E = 0
        for u in range(0, 10):
            for v in range(1, N + 1):
                if C[u] == A[v][u] == '1':
                    D[v] += 1

        for v in D:
            E += B[v][D[v]]

        if E > ans:
            ans = E

print(ans)
