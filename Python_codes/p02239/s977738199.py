from collections import deque


INFINITY = 10 ** 10
WHITE = 0
GRAY = 1
BLACK = 2


def breadth_first_search(u_start = 0):
    color[u_start] = GRAY
    d[u_start] = 0
    que.append(u_start)

    while que:
        u = que.popleft()
        for v in range(n):
            if matrix[u][v] and color[v] == WHITE:
                color[v] = GRAY
                d[v] = d[u] + 1
                que.append(v)
        color[u] = BLACK


# INPUT
n = int(input())


matrix = [[0] * n for _ in range(n)]

for i in range(n):

    u, k, *V = map(int, input().split())

    for v in V:
        v -= 1
        matrix[i][v] = 1


color = [WHITE] * n
d = [INFINITY] * n
que = deque([])

# PROCESS
breadth_first_search()


# OUTPUT
for i in range(n):
    if d[i] == INFINITY:
        distance = -1
    else:
        distance = d[i]

    print(i + 1, distance)

