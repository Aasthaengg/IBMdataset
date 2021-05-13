from collections import deque
n = int(input())

graph = [[] for i in range(n)]

for i in range(n-1):
    a, b, c = map(int, input().split())

    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

q_num, k = map(int, input().split())

seen = [-1 for i in range(n)]
seen[k-1] = 0


q = deque()

q.append((k-1, 0))

while len(q) > 0:
    cur = q.popleft()

    cur_node = cur[0]
    cur_cost = cur[1]

    for nx in graph[cur_node]:
        nx_node = nx[0]
        nx_cost = cur_cost + nx[1]

        if seen[nx_node] < 0:
            seen[nx_node] = nx_cost
            q.append((nx_node, nx_cost))

queries = []

for i in range(q_num):
    queries.append(list(map(int, input().split())))


for query in queries:
    print(seen[query[0]-1] + seen[query[1]-1])
