import sys
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(input())


from collections import deque
todo = deque()
seen = [[False] * W for _ in range(H)]
route= [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if A[y][x] == '#':
            todo.append((x, y))
            seen[y][x] = True



dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = -1
while todo:
    cnt += 1
    for _ in range(len(todo)):
        x, y = todo.popleft()
        #print(x, y)
        for i in range(4):
            if 0 <= x + dx[i] < W and 0 <= y + dy[i] < H:
                if seen[y + dy[i]][x + dx[i]] == False:
                    route[y + dy[i]][x + dx[i]] = route[y][x] + 1
                    seen[y + dy[i]][x + dx[i]] = True
                    todo.append((x + dx[i], y + dy[i]))

#print(seen)
# print(route)
# M = 0
# for y in range(H):
#     for x in range(W):
#         M = max(M, route[y][x])
# print(M)
print(cnt)