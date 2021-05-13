from collections import deque
n,m = map(int,input().split())
V = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    V[a].append([b,i])
    V[b].append([a,i])
ans = 0
for i in range(m):
    q = deque([])
    reach = [0] + [-1]*n
    q.append(1)
    reach[1] = 0
    while q:
        x = q.popleft()
        for X,j in V[x]:
            if j == i:
                pass
            else:
                if reach[X] == -1:
                    q.append(X)
                    reach[X] = 0
    if -1 in reach:
        ans += 1
print(ans)