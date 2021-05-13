from collections import deque
import sys


H, W = [int(_) for _ in input().split()]

M = []
q = deque([])
for i in range(H):
    A = input()
    M.append(list(A))
    for j in range(W):
        if A[j] == '#':
            q.append([j, i, 0])

depth_now = 0
depth = 0
count = 0
while len(q) > 0:
    p = q.popleft()
    x = p[0]
    y = p[1]
    depth = p[2]
    if x - 1 >= 0 and M[y][x-1] == '.':
        q.append([x-1, y, depth+1])
        M[y][x-1] = '#'
    if x + 1 < W and M[y][x+1] == '.':
        q.append([x+1, y, depth+1])
        M[y][x+1] = '#'
    if y - 1 >= 0 and M[y-1][x] == '.':
        q.append([x, y-1, depth+1])
        M[y-1][x] = '#'
    if y + 1 < H and M[y+1][x] == '.':
        q.append([x, y+1, depth+1])
        M[y+1][x] = '#'
print(depth)
