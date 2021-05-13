import itertools

N, M, r = map(int, input().split())
R = list(map(int, input().split()))
E = [[10 ** 20 if i != j else 0 for i in range(N)] for j in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    E[A][B] = C
    E[B][A] = C

for d in range(N):
    for v in range(N):
        for w in range(N):
            E[v][w] = min(E[v][w], E[w][v], E[v][d] + E[d][w])
            E[w][v] = E[v][w]

res = 10 ** 20
for case in itertools.permutations(R):
    tmp = 0
    c = list(case)
    for i in range(r - 1):
        tmp += E[c[i] - 1][c[i + 1] - 1]
    res = min(res, tmp)

print(res)