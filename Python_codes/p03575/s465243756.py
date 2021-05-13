n,m=map(int,input().split())
all_edge=[]
for i in range(m):
    a,b=map(int,input().split())
    all_edge.append([a-1,b-1])

def dfs(lst):
    visited=[None]*n
    visited[0]=1
    stack=[]
    for i in lst[0]:
        stack.append(i)
    while stack:
        new=stack.pop()
        if visited[new]==None:
            visited[new]=1
            for i in lst[new]:
                stack.append(i)
    if None in visited:
        return True
    else:
        return False

ans=0
for i in range(m): #橋の回数
    edge=[[] for _ in range(n)]
    for j in range(m): #1個除外する
        if i==j:
            continue
        a=all_edge[j][0]
        b=all_edge[j][1]
        edge[a].append(b)
        edge[b].append(a)
    if dfs(edge):
        ans+=1
print(ans)