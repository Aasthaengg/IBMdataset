from sys import stdin
readline=stdin.readline

#入力
n=int(readline())
m=n+1
u,k,v=[0]*m,[0]*m,[0]*m
for i in range(1,m):
    u[i],k[i],*v[i]=map(int,readline().split())

d=[0]*m
f=[0]*m
flags=[False]*m
t=0
def dfs(now):
    global t
    t+=1
    d[now]=t
    flags[now]=True
    for nex in v[now]:
        if flags[nex]==False:
            dfs(nex)
    t+=1
    f[now]=t
now=1
while True:
    dfs(now)
    for i in range(1,m):
        if flags[i]==False:
            now=i
            break
    else:
        break

for i in range(1,m):
    print(i,d[i],f[i])
