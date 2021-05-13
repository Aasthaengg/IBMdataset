# 幅優先探索 Breadth first search: BFS
import queue

n = int(input())
Adj = [[] for i in range(n)]
for i in range(n):
    dat = [int(i) for i in input().split()]
    Adj[dat[0] - 1] = dat[2:]

D = [-1 for i in range(n)]
D[0] = 0
Q = queue.Queue()
Q.put(1)
while not Q.empty():
    u = Q.get()
    for v in Adj[u - 1]:
        if D[v - 1] == -1:
            Q.put(v)
            D[v - 1] = D[u - 1] + 1

for i in range(n):
    print(i + 1, D[i])

