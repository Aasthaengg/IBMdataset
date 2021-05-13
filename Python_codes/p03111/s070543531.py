n,a,b,c = map(int, input().split())
l = [int(input()) for i in range(n)]
y=[0]*n
x=[]
def dfs(n,y,now):
    if now==n:
        z=y.copy()
        x.append(z)
        return
    for i in range(4):
        y[now]=i
        dfs(n,y,now+1)
dfs(n,y,0)
mi=1000000
for i in range(len(x)):
    al,bl,cl=0,0,0
    ac,bc,cc=0,0,0
    for j in range(n):
        if x[i][j]==1:
            al+=l[j]
            ac+=1
        if x[i][j]==2:
            bl+=l[j]
            bc+=1
        if x[i][j]==3:
            cl+=l[j]
            cc+=1
    if ac!=0 and bc!=0 and cc!=0:
        ans=abs(a-al)+abs(b-bl)+abs(c-cl)+10*(ac+bc+cc-3)
        mi=min(mi,ans)
print(mi)
