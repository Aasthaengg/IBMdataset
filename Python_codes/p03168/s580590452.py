n=int(input())
p=list(map(float,input().split()))
dp=[p[0],1-p[0]]
if n==1:
    print(p[0])
    exit()
for i in range(n-1):
    tmp=[]
    tmp.append(dp[0]*p[i+1])
    for j in range(i+1):
        tmp.append(dp[j]*(1-p[i+1])+dp[j+1]*p[i+1])    
    tmp.append(dp[-1]*(1-p[i+1]))
    dp=tmp
print(sum(dp[:n//2+1]))