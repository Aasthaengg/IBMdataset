from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())

start = []
goal = []
cost = []
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    start.append(A)
    goal.append(B)
    cost.append(C)
    start.append(B)
    goal.append(A)
    cost.append(C)

graph = csr_matrix((cost, (start, goal)), shape = (N, N))
can_reach_with_L = floyd_warshall(graph, directed = False)
can_reach_with_L[can_reach_with_L > L] = 0
ans = floyd_warshall(can_reach_with_L, directed = False, unweighted = True)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if ans[s][t] == float('inf'):
        print(-1)
    else:
        print(int(ans[s][t] + 0.5) - 1)
