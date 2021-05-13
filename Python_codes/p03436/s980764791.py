from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

cnt = 0
for i in s:
    cnt += i.count('.')

queue = deque([[0, 0]])
visited = [[1] * w for _ in range(h)]
visited[0][0] = 0

def bfs():
    while len(queue) > 0:
        h1, w1 = queue.popleft()
        if h1 == h - 1 and w1 == w - 1:
            return visited[h1][w1]
        for k, l in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            n_h, n_w = h1 + k, w1 + l
            if n_h < 0 or n_w < 0 or n_h >= h or n_w >= w:
                continue
            if visited[n_h][n_w] == 1 and s[n_h][n_w] == '.':
                queue.append([n_h, n_w])
                visited[n_h][n_w] += visited[h1][w1]
    return -1
    
bfs = bfs()
ans = 0
if bfs == -1:
    ans = -1
else:
    ans = cnt - bfs - 1
print(ans)
