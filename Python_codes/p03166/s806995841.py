import sys

sys.setrecursionlimit(10**9)

def dfs(n,arr,visited):
    for i in graph[n]:
        if visited[i]==False:
            arr[n]=max(arr[n],dfs(i,arr,visited)+1)
            visited[i]=True
        else:
            arr[n]=max(arr[n],arr[i]+1)
    return arr[n]

n,m=map(int,input().split())

graph=[[] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    if a!=b:
        graph[a-1].append(b-1)

visited=[False for i in range(n)]

arr=[0 for i in range(n)]

for i in range(n):
    if visited[i]==False:
        dfs(i,arr,visited)
print(max(arr))
