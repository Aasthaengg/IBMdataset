n,m = map(int, input().split())
link = [[] for _ in range(n)]
for i in range(m):
    tmp = list(map(int,input().split()))
    link[tmp[0]-1].append(tmp[1]-1)
s,t = map(int, input().split())

from collections import deque
Q = deque()
Q.append([s-1,0,0])
visited = [[] for _ in range(n)]
visited[s-1]=[0]

while Q:
    now,kkp,cnt = Q.popleft()
    nxt_kkp = (kkp+1)%3
    for nxt in link[now]:
        if nxt == (t-1) and nxt_kkp == 0:
            print((cnt+1)//3)
            exit()
        if nxt_kkp in visited[nxt]:
            continue
        visited[nxt].append(nxt_kkp)
        Q.append([nxt,nxt_kkp,cnt+1])

print(-1)