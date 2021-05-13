import sys


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

P = [None] * (H * W + 1)
P[0] = (0, 0)
for i in range(H):
    for j in range(W):
        P[A[i][j]] = (i, j)

S = [0] * (H * W + 1)
for i in range(1, H * W + 1):
    pi = max(0, i - D)
    S[i] = S[pi] + distance(P[pi], P[i])

ans = []
for q in sys.stdin.readlines():
    L, R = map(int, q.split())
    # ans.append(S[R] - S[L])
    print(S[R] - S[L])

# print(*ans, sep='\n')
