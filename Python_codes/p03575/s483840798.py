from copy import deepcopy
from collections import deque
N, M = map(int, input().split())
adj_mat = [[-float('inf') for i in range(N)] for j in range(N)]
ls = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    ls.append([a, b])
    adj_mat[a][b], adj_mat[b][a] = 1, 1

ans = 0
for i in range(M):
    adj_mat_copy = deepcopy(adj_mat)
    adj_mat_copy[ls[i][0]][ls[i][1]] = -float('inf')
    adj_mat_copy[ls[i][1]][ls[i][0]] = -float('inf')
    st = deque([])
    visited = [-1 for i in range(N)]
    st.append(0)
    visited[0] = 1
    while st:
        l = st.pop()
        for j, node in enumerate(adj_mat_copy[l]):
            if node == 1 and visited[j] != 1:
                st.append(j)
                visited[j] = 1
    if sum(visited) != N:
        ans += 1
print(ans)