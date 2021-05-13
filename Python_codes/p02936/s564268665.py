import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
Edges = list([] for _ in range(N))
for i in range(N-1):
    a, b = map(int, input().split())
    Edges[a-1].append(b-1)
    Edges[b-1].append(a-1)
P = [0 for _ in range(N)]
for i in range(Q):
    p, x = map(int, input().split())
    P[p-1] += x

gone = [False for _ in range(N)]

def dfs(counter, count, cur_node):
    count += P[cur_node]
    gone[cur_node] = True
    counter[cur_node] += count
    for next_node in Edges[cur_node]:
        if gone[next_node]:
            continue
        dfs(counter, count, next_node)

counter = [0 for _ in range(N)]
dfs(counter, 0, 0)

for c in counter:
    print(c)