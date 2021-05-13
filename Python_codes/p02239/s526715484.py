import sys

def bfs():
    global V, D

    D[1] = 0
    children = V[1]
    d = 1
    while len(children) != 0 :
        new = []
        for child in children:
            if D[child] == -1:
                D[child] = d
                new += V[child]
        children = new
        d += 1

lines = sys.stdin.readlines()
n = int(lines[0])
V = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    v = map(int, lines[i].split())
    V[v[0]] = v[2:]
D = [-1] * (n + 1)
bfs()

for i in range(1, n + 1):
    print i, D[i]