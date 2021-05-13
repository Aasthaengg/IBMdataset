H, W, D = map(int, input().split())
T = []
P = {}
for i in range(H):
    A = list(map(int, input().split()))
    T.append(A)
Q = int(input())
for i in range(H):
    for j in range(W):
        P[T[i][j]] = [i, j]

Jump = [[0] for _ in range(D+1)]
for i in range(1, D+1):
    total = 0
    for j in range(i, H*W+1-D, D):
        total += abs(P[j+D][0] - P[j][0]) + abs(P[j+D][1] - P[j][1])
        Jump[i].append(total)
Ans = []
for i in range(Q):
    L, R = map(int, input().split())
    k = L % D
    start = L//D
    end = R//D
    if k == 0:
        k += D
        start -= 1
        end -= 1
    Ans.append(Jump[k][end] - Jump[k][start])

for i in range(Q):
    print(Ans[i])