n = input()

time = []
time.append(0)

d = [0 for i in xrange(n + 1)]
f = [0 for i in xrange(n + 1)]
color = ['WHITE' for i in xrange(n + 1)]

graph_map = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]

for i in xrange(1, n + 1):
    tmp = map(int, raw_input().split())
    for j in xrange(tmp[1]):
        graph_map[i][tmp[j + 2]] = 1

def dfs(u):
    color[u] = 'GRAY'
    time[0] += 1
    d[u] = time[0]
    for v in xrange(1, n + 1):
        if graph_map[u][v] == 1 and color[v] == 'WHITE':
            dfs(v)
    color[u] = 'BLACK'
    time[0] += 1
    f[u] = time[0]

for i in xrange(1, n + 1):
    if color[i] == 'WHITE':
        dfs(i)

for i in xrange(1, n + 1):
    print "%d %d %d" % (i, d[i], f[i])