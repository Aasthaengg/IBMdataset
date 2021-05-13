n, m = map(int, input().split())
graph = {i:[] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for dst in graph[0]:
    if n-1 in graph[dst]:
        print('POSSIBLE')
        exit()
else:
    print('IMPOSSIBLE')