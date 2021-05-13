from collections import deque
NegInf = -float('inf')


n, m, p = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c-p))


def bellman_ford(vst, graph, node_num, NegInf):
    costs = [NegInf] * node_num
    costs[0] = 0
    v_nows = set([vst])
    for _ in range(n):
        v_changeds = set()
        for v_from in v_nows:
            for v_to, cost in graph[v_from]:
                c2 = costs[v_from] + cost
                if c2 > costs[v_to]:
                    costs[v_to] = c2
                    v_changeds.add(v_to)
        v_nows = v_changeds



    if not v_changeds:
        return costs

    for i in v_nows:
        costs[i] = NegInf

    que = deque(v_nows)
    while que:
        v_from = que.popleft()
        for v_to, cost in graph[v_from]:
            if costs[v_to] != NegInf:
                costs[v_to] = NegInf
                que.append(v_to)
    return costs


costs = bellman_ford(0, graph, n, -float('inf'))
if costs[n-1] == NegInf:
    print(-1)
else:
    print(max(0, costs[n-1]))