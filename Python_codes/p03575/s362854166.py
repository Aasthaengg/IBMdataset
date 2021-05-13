n,m=map(int,input().split())
edge=[[] for _ in range(n+1)]
eab=[]
for i in range(m):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
    eab.append([a-1,b-1])
 
def dfs(visited,count,node):
    visited[node]=True
    count+=1
    ev=edge[node]
    for node in ev:
        if visited[node]:
            continue
        else:
            count=dfs(visited,count,node)
    return count

ans=0
for i in range(m):
    a,b=eab[i]
    edge[a].remove(b)
    edge[b].remove(a)
    ci=dfs([False for _ in range(n)],0,0)
    if ci!=n:
        ans+=1
    edge[a].append(b)
    edge[b].append(a)
print(ans)