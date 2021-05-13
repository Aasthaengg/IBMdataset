n = int(input())
g = [set() for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)

def dfs(s):
    visited = [-1]*n
    visited[s] = 0
    temp = [s]
    lst = []
    while temp:
        p = temp.pop()
        for a in g[p]:
            if visited[a] != -1:continue
            visited[a] = visited[p] + 1
            temp.append(a)
    return visited

lst0 = dfs(0)
lstn = dfs(n-1)
cnt = 0
for i in range(n):
    if lst0[i] <= lstn[i]: cnt += 1

if cnt > n - cnt: print('Fennec')
else:print('Snuke')