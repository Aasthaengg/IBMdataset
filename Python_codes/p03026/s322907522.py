*D, = open(0)
n = int(D[0])

edge = [[] for _ in range(n+1)]
v_val = [0 for _ in range(n+1)]

dist = {}

for i in range(1, n):
    a, b = map(int, D[i].split())
    edge[a].append(b)
    edge[b].append(a)
c = list(map(int, D[n].split()))
c = sorted(c, reverse=True)

start = None
for i in range(1,len(edge)):
    if len(edge[i])==1:
        start = i
        break

        
import sys
sys.setrecursionlimit(10**7)


def visit(edge, start, visited, order):
    visited[start] = True
    order.append(start)
    
    for node in edge[start]:
        if not visited[node]:
            visit(edge, node, visited, order)
    
    return 

visited = [False for _ in range(len(edge))]
order = []
visit(edge, start, visited, order)

# calculate cost
v_val = [0 for _ in range(len(c)+1)]
for i, it in enumerate(order):
    v_val[it] = c[i]
    
print(sum(c[1:]))
print(' '.join(map(str, v_val[1:])))