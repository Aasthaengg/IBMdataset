def dfs(u):
    global time
    time+=1
    color[u]='gray'
    d[u]+=time
    for v in xrange(n):
        if m[u][v]!=0 and color[v]=="white":
            dfs(v)
    time+=1
    color[u]="black"
    f[u]+=time
    

n=input()
info=[0]*n
color=["white"]*n
m=[[0]*n for _ in xrange(n)]
d=[0]*n
f=[0]*n
for i in xrange(n):
    info[i]=map(int,raw_input().split())
    if info[i][1]==0:
        pass
    else:
        for j in info[i][2:]:
            m[i][j-1]=j
time=0
for i in xrange(n):
    if color[i]=="white":
        dfs(i)
for i in xrange(n):
    print i+1,d[i],f[i]