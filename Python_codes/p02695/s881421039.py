import itertools
N, M, Q = map(int, input().split())
A = [0] * Q
B = [0] * Q
C = [0] * Q
D = [0] * Q

for i in range(Q):
    a, b, c, d = map(int, input().split())
    A[i] = a
    B[i] = b
    C[i] = c
    D[i] = d
X = list(itertools.combinations_with_replacement([a for a in range(1,M+1)],N))

cnt = [0] * (len(X))
for k in range(len(X)):
    for l in range(Q):
        if X[k][B[l] - 1] - X[k][A[l] - 1] == C[l]:
            cnt[k] += D[l]

print(max(cnt))