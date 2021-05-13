from collections import defaultdict, deque
d = defaultdict(list)
n = int(input())
for i in range(n-1):
    u, v = map(int, input().split())
    u-=1
    v-=1
    d[u].append(v)
    d[v].append(u)
c = list(map(int, input().split()))
c.sort(reverse = True)
vis = [0 for i in range(n)]
q = deque([])
q.append(0)
vis[0] = c[0]
ind = 1
while(q):
    f = q.popleft()
    for i in d[f]:
        if not vis[i]:
            vis[i] = c[ind]
            ind+=1
            q.append(i)
print(sum(vis) - c[0])
print(*vis)