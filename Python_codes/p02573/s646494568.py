import collections

n,m = map(int,input().split())
friend = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    friend[a].append(b)
    friend[b].append(a)

q = collections.deque()
visited = [0 for i in range(n)]

ans = 0
for i in range(n):
    tmp = 0
    if visited[i] == 0:
        visited[i] = 1
        tmp += 1
        for j in friend[i]:
            if visited[j] == 0:
                visited[j] = 1
                tmp += 1
                q.append(j)
        while q:
            s = q.pop()
            for k in friend[s]:
                if visited[k] == 0:
                    visited[k] = 1
                    tmp += 1
                    q.append(k)
    ans = max(ans,tmp)

print(max(ans,1))