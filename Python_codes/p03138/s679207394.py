n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
x=0
dp=[0]*40
for i in a:
    for j in range(40):
        if i&(1<<j):
            dp[j]+=1

for i in range(39,-1,-1):
    if x+ (1<<i) >k:
        continue
    if dp[i]<(n+1)//2:
        x+=(1<<i)





for  i in a:
    ans+=x^i
print(ans)