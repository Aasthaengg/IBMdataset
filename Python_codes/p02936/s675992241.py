import sys
sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N - 1)]
px = [list(map(int, input().split())) for i in range(Q)]
 
root = [[] for i in range(N + 1)]
result = [0 for i in range(N + 1)]
 
for i in range(N - 1):
    a = ab[i][0]
    b = ab[i][1]
    root[a].append(b)
    root[b].append(a)
 
for i in range(Q):
    p = px[i][0]
    x = px[i][1]
    result[p] = result[p] + x
 
 
def dfs(now, prev):
    if len(root[now]) == 0:
        return
    else:
        for i in range(len(root[now])):
            next_point = root[now][i]
            if next_point == prev:
                continue
            else:
                result[next_point] = result[next_point] + result[now]
                dfs(next_point, now)
 
 
dfs(1, -1)
print(*result[1:])