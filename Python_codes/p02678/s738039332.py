# coding: utf-8
# Your code here!
from collections import deque

N,M=map(int,input().split())

way=[[] for i in range(N)]

for _ in range(M):
    A,B=map(int,input().split())
    way[A-1].append(B-1)
    way[B-1].append(A-1)

visited=[-1 for i in range(N)]
visited[0]=0
dq=deque([0]) #loc,value

while dq:
    temp=dq.popleft()
    for item in way[temp]:
        if visited[item]==-1:
            visited[item]=temp
            dq.append(item)

if -1 in visited:
    print("No")
else:
    print("Yes")
    for item in visited[1:]:
        print(item+1)
