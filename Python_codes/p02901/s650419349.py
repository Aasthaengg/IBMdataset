n,m=map(int,input().split())
dp=[float("inf")]*(1<<n)
b=[True]*(1<<n)
p=[]
k=0
for i in range(m):
    k=0
    a,_=map(int,input().split())
    c=list(map(int,input().split()))
    for cc in c:
        k+=1<<(cc-1)
    if b[k]:
        b[k]=False
    dp[k]=min(dp[k],a)
    p.append(k)
while True:
    d=[]
    for i in p:
        for j in p:
            if dp[i|j]>dp[i]+dp[j]:
                dp[i|j]=dp[i]+dp[j]
                if b[i|j]:
                    b[i|j]=False
                    d.append(i|j)
    if len(d)==0:
        break
    for oo in d:
        p.append(oo)
if dp[-1]==float("inf"):
    print(-1)
else:
    print(dp[-1])