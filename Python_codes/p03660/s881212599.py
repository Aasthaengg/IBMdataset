import sys
input = sys.stdin.readline


n = int(input())
edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

seen = [-1] * n
todo = [(0, 0)]

while todo:
    node, prev = todo.pop()
    if seen[node] != -1:
        continue

    seen[node] = prev
    for to in edges[node]:
        if seen[to] != -1:
            continue
        todo.append((to, node))


colors = [0] * n

node = n-1
goal_to_start = [n-1]
while node:
    node = seen[node]
    goal_to_start.append(node)

length = len(goal_to_start)
limit = (length) // 2

colors = [0] * n
for node in goal_to_start[:limit]:
    colors[node] = 2

for node in goal_to_start[limit:]:
    colors[node] = 1

fennec_todo = [node for node in range(n) if colors[node] == 1]
snuke_todo = [node for node in range(n) if colors[node] == 2]


def paint(todo, my_color):
    while todo:
        node = todo.pop()
        for to in edges[node]:
            if colors[to]:
                continue

            colors[to] = my_color
            todo.append(to)


paint(fennec_todo, 1)
paint(snuke_todo, 2)

feccec_count = len([color for color in colors if color == 1])
snuke_count = len([color for color in colors if color == 2])

if feccec_count > snuke_count:
    print('Fennec ')

else:
    print('Snuke ')
