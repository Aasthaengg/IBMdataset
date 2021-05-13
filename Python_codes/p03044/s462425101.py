n = int(input())
g = [[]for i in range(n)]
def swap(n):
    if n == 1:
        return 0
    else:
        return 1
for i in range(n-1):
    u,v,w = map(int,input().split())
    u = u-1
    v = v-1
    w = w%2
    g[u].append([v,w])
    g[v].append([u,w])
ans = [-1 for i in range(n)]
from collections import deque
d = deque([[0,0]]) #左は頂点の数字、右は塗った色
while d:
    p,q = d.pop()
    ans[p] = q
    for j,w in g[p]:
        if ans[j] != -1:
            continue
        else:
            if w == 1:
                d.append([j,swap(q)])
            else:
                d.append([j,q])
for i in range(n):
    print(ans[i])