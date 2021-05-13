n=int(input())
sche=[0 for i in range(n)]
#ith store,jth day ,kth time >sche[i][2*(j-1)+(k-1)]
for h in range(n):
    sche[h]={i for i,v in enumerate(input().split()) if v=="1" }
profit=[list(map(int,input().split())) for i in range(n)]
ans=-float("INF")
for i in range(1,1024):
    op={j for j in range(10) if (i>>j)%2}
    pre=0
    for g in range(n):
        pre+=profit[g][len(op&sche[g])]
    ans=max(pre,ans)
print(ans)