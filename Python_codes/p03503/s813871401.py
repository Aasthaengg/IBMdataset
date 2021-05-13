n=int(input())
f=[]
for i in range(n):
    f.append(list(map(int,input().split())))
p=[]
for i in range(n):
    p.append(list(map(int,input().split())))
a=0
ans=-(10**10)
for k in range(1,1024):
    a=0
    x=bin(k)
    y=[0]*10
    for i in range(2,len(x)):
        y[10-len(x)+i]+=int(x[i])
    for i in range(n):
        m=0
        t=0
        for j in range(10):
            if y[j]+f[i][j]==2:
                t+=1
        m+=p[i][t]
        a+=m
    ans=max(a,ans)
print(ans)