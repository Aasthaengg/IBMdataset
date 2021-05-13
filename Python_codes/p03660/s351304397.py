import itertools
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n=int(input())
edge = [[] for _ in range(n)]
visited = [0]*n
for i in range(n-1):
    a,b=map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
path = []
def dfs(i):
    visited[i]=1
    if(i==n-1):
        return 1
    else:
        for j in edge[i]:
            if(not visited[j]):
                if(dfs(j)):
                    if(i!=0):
                        path.append(i)
                    return i

    return 0



dfs(0)
s = 0
f = 0
visited_new = [-1]*n
path_l = len(path)
for i in range(path_l):
    if(i<(path_l//2)):
        visited_new[path[i]]=1
        s+=1
    else:
        visited_new[path[i]]=2
        f+=1

visited_new[n-1]=3
visited_new[0]=3
que=deque()
que.append(n-1)
while que:
    v=que.popleft()
    for next_v in edge[v]:
        if visited_new[next_v]==2:continue
        if visited_new[next_v]==1 or visited_new[next_v]==-1:
            visited_new[next_v]=3
            que.append(next_v)
            s+=1
que.append(0)
while que:
    v=que.popleft()
    for next_v in edge[v]:
        if visited_new[next_v]==3:continue
        if visited_new[next_v]==2 or visited_new[next_v]==-1:
            visited_new[next_v]=3
            que.append(next_v)
            f+=1
if(f>s):
    print("Fennec")
else:
    print("Snuke")
