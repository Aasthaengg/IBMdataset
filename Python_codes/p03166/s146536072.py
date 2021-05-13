from collections import defaultdict, deque

def topological_sort(vertex:list, edge:list):
    graph = {i: [] for i in vertex}
    for i, j in edge:
        graph[i].append(j)
        
    inp_cnt = defaultdict(int)
    outs = defaultdict(list)
    for inp, out in edge:
        inp_cnt[out] += 1
        outs[inp].append(out)

    result = []
    queue = deque([i for i in vertex if inp_cnt[i]==0])
    while queue:
        v = queue.popleft()
        result.append(v)
        for v2 in outs[v]:
            inp_cnt[v2] -= 1
            if inp_cnt[v2] == 0:
                queue.append(v2)
    return result

N, M = map(int, input().split())
vertex = list(range(1, N+1))
edge = [list(map(int, input().split())) for _ in range(M)]
graph = {i: [] for i in vertex}
for i, j in edge:
    graph[i].append(j)

sorted_vertecies = topological_sort(vertex, edge)
dp = [0] * (N+1)
for i in sorted_vertecies:
    ends = graph[i]
    for j in ends:
        dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))