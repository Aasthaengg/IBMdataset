from collections import deque
n , m = map(int,input().split())
z = [[] for i in range(n)]
for i in range(m):
    l , r , d = map(int,input().split())
    z[l-1].append((r-1,d))
    z[r-1].append((l-1,-d))

visit = [False for i in range(n)]
x = [-1 for i in range(n)]
for i in range(n):
    if visit[i]:
        continue
    visit[i] = True
    q = deque()
    q.append(i)
    x[i] = 0
    while q:
        now = q.popleft()
        for t , d in z[now]:
            if not visit[t]:
                visit[t] = True
                x[t] = x[now] + d
                q.append(t)
            elif visit[t]:
                if x[t] - x[now] != d:
                    print("No")
                    exit()
print("Yes")