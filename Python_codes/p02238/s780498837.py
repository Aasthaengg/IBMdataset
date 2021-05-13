n=int(input())
seen=[-1]*n
first_order=[0]*n
last_order=[0]*n
cnt=0
def dfs(G,s):
    global cnt
    first_order[s]=cnt+1
    cnt+=1
    seen[s]=1
    for nv in G[s]:
        if(seen[nv]!=-1):
            continue
        dfs(G,nv)
    last_order[s]=cnt+1
    cnt+=1

G=[[] for i in range(n)]
for i in range(n):
    li=list(map(int,input().split()))
    for x in range(2,len(li)):
        G[i].append(li[x]-1)
for i in range(n):
    if(seen[i]==-1):
        dfs(G,i)
for i in range(n):
    print(i+1,first_order[i],last_order[i])
