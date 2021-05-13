def dfs(adjlist,v):
    global d,f,t
    d[v-1]=t
    t+=1
    for node in adjlist[v-1]:
        if d[node-1]<0 and node>0:
            dfs(adjlist,node)
    f[v-1]=t
    t+=1

n=int(input())
adjlist=[list(map(int,input().split()))[2:] for _ in range(n)]
d=[-1]*n
f=[-1]*n
t=1
for i in range(1,n):
    if d[i-1]<0:
       dfs(adjlist,i)
for i in range(n):
    print("{} {} {}".format(i+1,d[i],f[i]))
