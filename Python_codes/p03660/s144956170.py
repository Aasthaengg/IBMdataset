n = int(input())
link = [[] for _ in range(n)]
for i in range(n-1):
    tmp = list(map(int,input().split()))
    link[tmp[0]-1].append(tmp[1]-1)
    link[tmp[1]-1].append(tmp[0]-1)
 
from collections import deque
Q = deque()
Q.append(0)
visited=[-1]*n
visited[0]=1
prev=[-1]*n
 
while Q:
    now = Q.popleft()
    for nxt in link[now]:
        if visited[nxt]!=-1:
            continue
        visited[nxt]=1
        Q.append(nxt)
        prev[nxt]=now
 
rt=[n-1]
now=n-1
while prev[now]!=-1:
    now=prev[now]
    rt.append(now)
rt.reverse()
cut= -(-len(rt)//2)
f_node=rt[cut-1]
s_node=rt[cut]
 
Q = deque()
Q.append([0,0]) # 0 is f, 1 if s
visited=[-1]*n
visited[0]=0
 
while Q:
    now,fs = Q.popleft()
    for nxt in link[now]:
        nxt_fs=fs
        if now==f_node and nxt==s_node:
            nxt_fs=1
        if visited[nxt]!=-1:
            continue
        visited[nxt]=nxt_fs
        Q.append([nxt,nxt_fs])
s_score = sum(visited)
f_score = n-s_score
if s_score >= f_score:
    print("Snuke")
else:
    print("Fennec")