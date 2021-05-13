from collections import deque

H, W = map(int, input().split())
S = [input() for i in range(H)]
l = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            l.append((i, j))

m = -1
N = len(l)
for i in range(N-1):
    for j in range(i+1, N):
        start = l[i]
        goal = l[j]
        visited = [[-1]*W for i in range(H)]
        d = deque()
        d.appendleft(start)
        visited[start[0]][start[1]] = 0
        while d:
            now = d.pop()
            for direction in directions:
                next = (now[0]+direction[0], now[1]+direction[1])
                if not (next[0] in range(H) and next[1] in range(W)):
                    continue
                if visited[next[0]][next[1]] != -1:
                    continue
                if S[next[0]][next[1]] == '.':
                    visited[next[0]][next[1]] = visited[now[0]][now[1]] + 1
                    d.appendleft(next)
                if next == goal:
                    m = max(visited[goal[0]][goal[1]], m)
                    d = deque()

print(m)