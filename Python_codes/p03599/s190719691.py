a,b,c,d,e,f=map(int,input().split())

a *=100
b *=100
DP=[[0,0] for _ in range(f+3000)]
DP[a][0]=a
DP[b][0]=b

for i in range(f+1):
    if DP[i][0]==0:continue
    for j in a,b:
        if i+j<=f:
            if DP[i][1]*100/(i+j)>=DP[i+j][1]*100/(i+j):
                DP[i+j]=[i+j,DP[i][1]]
    for j in c,d:
        if i+j<=f:
            if 100*(DP[i][1]+j)/(i+j)<=100*e/(100+e):
                if 100*(DP[i][1]+j)/(i+j)>=100*(DP[i+j][1])/(i+j):
                    DP[i+j]=[i+j,DP[i][1]+j]

ans,water=0,[a,0]
for x,y in DP:
    if x==0:continue
    if 100*y/x>ans:
        ans=100*y/x
        water=[x,y]
print(*water)