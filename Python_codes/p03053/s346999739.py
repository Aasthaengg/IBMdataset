from collections import deque

H, W = map(int, input().split())
A = [[0] * (W + 2)] + [[0] + [H * W] * W + [0] for _ in range(H)] + [[0] * (W + 2)]
que = deque()
for i in range(1, H+1):
    for j, a in enumerate(list(input())):
        if a == '#':
            A[i][j+1] = 0
            que.append((i, j + 1))

step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = 0
while que:
    h, w = que.popleft()
    for dh, dw in step:
        nh = h + dh
        nw = w + dw
        if A[h][w] + 1 < A[nh][nw]:
            A[nh][nw] = A[h][w] + 1
            res = max(res, A[nh][nw])
            que.append((nh, nw))
print(res)