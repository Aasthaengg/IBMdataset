import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford, connected_components
from scipy.sparse.csgraph._shortest_path import NegativeCycleError

input = sys.stdin.buffer.readline


N, M = map(int, input().split())
starts = []
ends = []
costs = []
for _ in range(M):
    a, b, c = map(int, input().split())
    starts.append(a-1)
    ends.append(b-1)
    if c != 0:
        costs.append(-c)
    else:
        costs.append(sys.float_info.epsilon)

look_for_loop = csr_matrix((costs + [0], (starts + [N-1], ends + [0])), shape = (N, N))
_, labels = connected_components(look_for_loop, connection = "strong")
mask = (labels == labels[0])

graph = csr_matrix((costs, (starts, ends)), shape = (N, N)).toarray()
graph = graph[mask, :][:, mask]

try:
    ans = bellman_ford(graph, directed = True, indices = [0])[0][-1]
    ans = int(round(-ans))
except NegativeCycleError:
    ans = "inf"

print(ans)
