n=int(input())
g=[]
for i in range(n):
    u,k,*varray= map(int,input().split())
    g.append(varray)

time = 1
d= [-1]* n
f= [-1]* n

def dfs(src):
    global time
    d[src]= time
    time+=1
    for i in g[src]:
        if d[i-1]== -1:
            dfs(i-1)
    f[src]= time
    time+=1

for i in range(n):
    if d[i]== -1:
        dfs(i)
for i in range(n):
    print(i+1,d[i],f[i])
