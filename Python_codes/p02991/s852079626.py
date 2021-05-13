from sys import stdin
from collections import defaultdict
from collections import deque

N,M = list(map(int,stdin.readline().split()))
Cs = [tuple(map(int,stdin.readline().split())) for _ in range(M)]
S,T = list(map(int,stdin.readline().split()))

INF = 10 ** 15
# visit = [False] * ( (N + 1) * 3 )
dist  = [-1] * ( (N) * 3 + 1 )
graph_connection = defaultdict(lambda :[])
graph_cost = defaultdict(lambda :defaultdict(lambda :INF))
#
# def dfs(v,dist_before):
#
#     dist[v] = dist_before + 1
#     next_vertexs = graph_connection[v]
#     for next_v  in next_vertexs :
#         if dist[next_v] == -1:
#             dfs(next_v,dist[v])
#     return 0
#

for cost in  Cs:
    a,b= cost
    for i in range(0,3):
        from_v = a + (i) * N
        to_v = b + (i + 1) % 3 * N
        graph_connection[from_v].append(to_v )

        # from_v = b + (i) * N
        # to_v = a + (i + 1) % 3 * N
        # graph_connection[from_v].append(to_v )

# dist[S] = 0


que = deque()
#(from_v,to_v)
dist[S] = 0
que.append(S)
while len(que) != 0:
    from_v = que.popleft()
    nexts = graph_connection[from_v]
    for next_v in nexts:
        if dist[next_v] == -1:
            dist[next_v] = dist[from_v] + 1
            que.append(next_v)

if dist[T] < 0:
    print(dist[T] )
else:
    print(dist[T]//3)
