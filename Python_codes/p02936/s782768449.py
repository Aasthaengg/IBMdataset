n, q = map(int, input().split())
Tree = [[] for _ in range(n+1)]
Counter = [0 for _ in range(n+1)]
AB = (tuple(map(int, input().split())) for _ in range(n-1))
PX = (tuple(map(int, input().split())) for _ in range(q))

for a,b in AB:
  Tree[a].append(b)
  Tree[b].append(a)
  
for p,x in PX:
  Counter[p] += x

P = [-1]*(n+1)

nodes = [1]
while nodes:
  parent = nodes.pop()
  for node_i in Tree[parent]:
    if P[parent]==node_i:
      continue
    P[node_i] = parent
    nodes.append(node_i)
    Counter[node_i] += Counter[parent]

print(*Counter[1:])