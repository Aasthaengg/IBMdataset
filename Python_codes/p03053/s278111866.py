from collections import deque
H, W = map(int, input().split())
A = [list(input()) for i in range(H)]
Q = deque()
h = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            Q.append([i, j])
        else:
            h += 1
Qtmp = deque()

yudrl = [0, 1, 0, -1]
xudrl = [1, 0, -1, 0]

c = 0
while h > 0:
    c += 1
    while len(Q) > 0:
        Qtmp.append(Q.pop())
    while len(Qtmp) > 0:
        q = Qtmp.pop()

        for i in range(4):
            y = q[0] + yudrl[i]
            x = q[1] + xudrl[i]

            if y < 0 or y > H - 1 or x < 0 or x > W - 1:
                continue
            if A[y][x] == '#':
                continue
            A[y][x] = '#'
            h -= 1
            Q.append([y, x])
print(c)