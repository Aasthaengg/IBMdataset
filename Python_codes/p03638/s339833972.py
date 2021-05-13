import sys
input = sys.stdin.readline
H, W = [int(x) for x in input().strip().split()]
N = int(input())
A = [int(x) for x in input().strip().split()]
M = [[-1] + [0] * (W) + [-1] for _ in range(H+2)]
M[0] = [-1] * (W+2)
M[-1] = [-1] * (W+2)

vec = [(0, 1), (1, 0), (0, -1), (-1, 0)]

k = 0
h, w = 1, 1
for i, a in enumerate(A, start=1):
    for _ in range(a):
        M[h][w] = i
        if M[h+vec[k][0]][w+vec[k][1]] != 0:
            k = (k + 1) % 4
        h += vec[k][0]
        w += vec[k][1]

for m in M[1:len(M)-1]:
    print(*m[1:len(m)-1])