from collections import defaultdict,deque
n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False]*(n+1)
que = deque([1])
visited[1] = True
ans = [-1]*(n+1)

while que:
    v = que.popleft()
    vlist = d[v]
    for next in vlist:
        if not visited[next]:
            que.append(next)
            visited[next] = True
            ans[next] = v

if -1 in ans[2:]:
    print('No')
    exit()
print('Yes')
for i in range(2,n+1):
    print(ans[i])