from collections import defaultdict as dd
n, q = map(int, input().split())
Connections = dd(list)
for i in range(n-1):
    a, b = map(int, input().split())
    Connections[a].append(b)
    Connections[b].append(a)

#Tree[node] -> children(list)
Tree = dd(list)
visited = set()
stack = [1]
while stack != []:
    temp = []
    for taregt_node in stack:
        for next_node in Connections[taregt_node]:
            if next_node not in visited:
                Tree[taregt_node].append(next_node)
                visited.add(taregt_node)
                temp.append(next_node)
    stack = temp
#print(Tree)

#Point[node] -> point
Point = dd(int)
for i in range(q):
    p, x = map(int, input().split())
    Point[p] += x
#print(Point)

Counter = dd(int)
#visited = set()
stack = [1]
Counter[1] = Point[1]
while stack != []:
    temp = []
    for target_node in stack:
        for next_node in Tree[target_node]:
            Counter[next_node] = Counter[target_node] + Point[next_node]
            temp.append(next_node)
    stack = temp
#print(Counter)

for i in range(1, n):
    print(Counter[i], end=" ")
print(Counter[n])