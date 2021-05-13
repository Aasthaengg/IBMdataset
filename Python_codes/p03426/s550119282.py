H, W, D = map(int, input().split())
A = tuple(tuple(map(int, input().split())) for _ in range(H))

pos = [0] * (H * W + 1)

for i in range(H):
    for j in range(W):
        pos[A[i][j]] = (i, j)

def L1(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

costs = []

for i in range(H * W + 1):
    costs.append(0 if i <= D else costs[i - D] + L1(pos[i - D], pos[i]))

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(costs[R] - costs[L])
