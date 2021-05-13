n = int(raw_input())
INF = 10000000
queue = []

def bfs(s):
    queue.append(s)
    d = [INF for i in range(n)]
    d[s] = 0
    while len(queue) != 0:
        u = queue.pop(0)
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != INF:
                continue
            d[v] = d[u] + 1
            queue.append(v)
    for i in range(n):
        if d[i] == INF:
            length = -1
        else:
            length = d[i]
        print "%d %d" %(i + 1, length)
        
M = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    tmp = map(int, raw_input().split())
    u = tmp[0]
    k = tmp[1]
    u -= 1
    for j in range(k):
        v = tmp[j + 2]
        v -= 1
        M[u][v] = 1
bfs(0)