import sys
# sys.stdin = open('input.txt')

def fillMatrix():
    for i in range(n):
        u, k, *v = map(int, input().split())
        for j in v:
            matrix[i][j-1] = 1

def dfs(u):
    global time
    status[u] = VISITING
    time += 1
    discoverTime[u] = time
    for v in range(n):
        if matrix[u][v] and status[v] == NOT_VISITED:
            dfs(v)
    status[u] = VISITED
    time += 1
    finishTime[u] = time


n = int(input())
matrix = [[0]*n for i in range(n)]
time = 0
discoverTime = [0] * n
finishTime = [0] * n

NOT_VISITED = 0 # WHITE
VISITING = 1 # GRAY
VISITED = 2 # BLACK
status = [NOT_VISITED] * n

fillMatrix()
# Calling dfs(0) alone cannot reach nodes not connected from 0
for i in range(n):
    if status[i] != VISITED:
        dfs(i)

for i in range(n):
    ans = []
    ans.append(i+1)
    ans.append(discoverTime[i])
    ans.append(finishTime[i])
    ans = map(str, ans)
    print(' '.join(ans))
