n = input()

d = [-1 for i in xrange(n + 1)]
Q = []

color = ['WHITE' for i in xrange(n + 1)]

graph_map = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]

for i in xrange(1, n + 1):
    tmp = map(int, raw_input().split())
    for j in xrange(tmp[1]):
        graph_map[i][tmp[j + 2]] = 1

color[1] = 'GRAY'
d[1] = 0
Q.append(1)

while len(Q) != 0:
    u = Q.pop(0)
    for v in xrange(1, n + 1):
        if graph_map[u][v] == 1 and color[v] == 'WHITE':
            color[v] = 'GRAY'
            d[v] = d[u] + 1
            Q.append(v)
    color[u] = 'BLACK'

for i in xrange(1, n + 1):
    print "%d %d" % (i, d[i])