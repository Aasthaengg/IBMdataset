from itertools import permutations
N, C = map(int, input().split())
D, P = [], [[0]*C for _ in range(3)]
for i in range(C):
    D.append(list(map(int, input().split())))
for i in range(N):
    for j, c in enumerate(map(int, input().split())):
        P[(i+j)%3][c-1] += 1
res = float("inf")
for q in permutations(range(C),3):
    tmp = 0
    for k in range(3):
        c = q[k]
        for i, p in enumerate(P[k]):
            tmp += D[i][c]*p
    res = min(tmp, res)
print(res)