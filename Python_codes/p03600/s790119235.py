def warshall(d, n):
    e = copy.deepcopy(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # print(d[i][k], d[k][j], d[i][j])
                if i == k or k == j:
                    continue
                if d[i][k] + d[k][j] < d[i][j]:
                    return []
                if d[i][k] + d[k][j] == d[i][j]:
                    # print(d[i][k], d[k][j], d[i][j], i,j,k)
                    e[i][j] = 0
                    e[j][i] = 0
    return e
    
import copy
n = int(input())
edges = []

graph = [list(map(int, input().split())) for i in range(n)]
e = warshall(graph, n)
if e == []:
    print(-1)
    exit()
# print(e)
edge_list = [[] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if e[i][j] > 0:
            edge_list[i].append((e[i][j], j))
        if j > i and e[i][j]:
            ans += e[i][j]

print(ans)
