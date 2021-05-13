# coding: utf-8
# Your code here!
from collections import deque

def bfs(num):
    if visited[num]==0:
        visited[num]=C.pop(-1)
        for item in way[num]:
            d.append(item)
    return

N=int(input())

ans=[-1]*N
way=[[]for i in range(N)]
visited=[0]*N

for _ in range(N-1):
    a,b=map(int,input().split())
    way[a-1].append(b-1)
    way[b-1].append(a-1)

C=list(map(int,input().split()))
C.sort()
#print(C)


d=deque([0])

while d:
    temp=d.popleft()
    if visited[temp]==0:
        bfs(temp)

ans=0
for i in range(N):
    for item in way[i]:
        ans+=min(visited[i],visited[item])

print(ans//2)
print(*visited)
    
