from collections import deque
n, m = map(int, input().split())
E = [[*map(lambda x: int(x)-1, input().split())] for _ in range(m)]
V = [[] for _ in range(n)]
for a,b in E:
    V[a].append(b)
    V[b].append(a)

def dfs(a,b,f,i):
    # if i>=n:
    #     return
    if vis[f] == 1: return
    vis[f] = 1
    # print('f',f)
    for t in V[f]:
        if f==a and t == b: continue
        # if t == b: continue
        if vis[t] == 1: continue
        # print(t)
        dfs(a,b,t,i+1)

ans = 0
for a, b in E:
    vis = [0]*n
    dfs(a,b,a,1)
    # print(a,b,vis)
    if vis[b] == 0:
        ans += 1
    # print('----')

# print(E)
# print(V)

print(ans)
