import sys
import queue
input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n+1)]
d = [-1 for _ in range(n+1)]
for _ in range(n):
    c = list(map(int,input().split()))
    g[c[0]] = c[2:]

depth = 0
q = queue.Queue()
p = queue.Queue()
q.put(1)
while not q.empty():
    while not q.empty():
        s = q.get()
        if d[s] < 0:
            d[s] = depth
            for i in g[s]:
                p.put(i)
    p, q = q, p
    depth += 1

for i in range(1,n+1):
    print (i,d[i])
