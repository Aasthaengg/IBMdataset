from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())

M = [[0] * n for i in range(n)]

d = [-1] * (n)
color = [WHITE] * (n)


time = 0

def dfs_visit(u):
    global time
    time += 1
    color[u] = GRAY
    d[u] = time
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v)
    color[u] = BLACK
    time += 1

def bfs(s):
    queue = deque([])
    queue.append(s)
    d[s] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != -1:
                continue
            d[v] = d[u] + 1
            queue.append(v)

    for i in range(n):
        print("%d %d" % (i+1, d[i]))


if __name__ == "__main__":
    for i in range(n):
        arr = list(map(int, input().split()))
        for v in (arr[2:]):
            M[arr[0]-1][v-1] = 1

    bfs(0)

