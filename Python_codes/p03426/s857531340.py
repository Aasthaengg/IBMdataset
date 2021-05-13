import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

######################################################

H, W, D = [int(_) for _ in input().split()]

A = [[int(_) for _ in input().split()]
     for _ in range(H)]

B = [None] * (H * W + 1)
for i in range(H):
    h = i * W
    for j in range(W):
        B[h + j] = (A[i][j], (i, j))
B[H * W] = (0, (-1, -1))
B = sorted(B, key=lambda x: x[0])
costs = [0] * (H * W + 1)
for i in range(H * W, 0, -1):
    if i + D <= H * W:
        costs[i] = costs[i + D] + abs(B[i][1][0] - B[i + D][1][0]) + abs(B[i][1][1] - B[i + D][1][1])

for i in range(int(input())):
    l,r = [int(_) for _ in input().split()]
    print(costs[l] - costs[r])

