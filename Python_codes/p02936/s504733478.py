from queue import Queue
def bfs(target, graph, scores):
    visited = [False]*len(graph)
    que = Queue()
    que.put(target)
    visited[target] = True
    while not que.empty():
        root = que.get()
        for dst in graph[root]:
            if visited[dst] is False:
                visited[dst] = True
                que.put(dst)
                scores[dst] += scores[root] 
    return scores 
n, q = map(int, input().split())
graph = {i:[] for i in range(0, n)}
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

scores = [0]*n
for _ in range(q):
    t, s = map(int, input().split())
    t -= 1
    scores[t] += s

ans = bfs(0, graph, scores)
for a in ans:
    print(a)