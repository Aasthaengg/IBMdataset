n = int(input())
Edge = [list(map(int,input().split())) for i in range(n-1)]

Graph = [[] for i in range(n)]
for edge in Edge:
    Graph[edge[0]-1].append(edge[1]-1)
    Graph[edge[1]-1].append(edge[0]-1)

Distance_1 = [-1 for i in range(n)]
Distance_1[0] = 0
Distance_n = [-1 for i in range(n)]
Distance_n[n-1] = 0

stack = [0]
while stack:
    node = stack.pop()
    for adj in Graph[node]:
        if Distance_1[adj] == -1:
            Distance_1[adj] = Distance_1[node] + 1
            stack.append(adj)

stack = [n-1]
while stack:
    node = stack.pop()
    for adj in Graph[node]:
        if Distance_n[adj] == -1:
            Distance_n[adj] = Distance_n[node] + 1
            stack.append(adj)

count = 0
for i in range(n):
    if Distance_1[i]<=Distance_n[i]:
        count += 1

if count > n-count:
    print('Fennec')
else:
    print('Snuke')