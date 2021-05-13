import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
graph = [0] + [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(graph, queue, color):
    is_bigraph = True
    while queue:
        current = queue.pop()
        current_color = color[current]

        for _next, dist in graph[current]:
            if color[_next] != - 1:
                if color[_next] != (color[current] + dist) % 2:
                    is_bigraph = False
            else:
                color[_next] = (color[current] + dist) % 2
                queue.append(_next)

    return is_bigraph

queue = [1]
color = [-1] + [-1] * n
color[1] = 0
if not dfs(graph, queue, color):
    print('Something wrong')
    sys.exit(1)

for c in color[1:]:
    print(c)
