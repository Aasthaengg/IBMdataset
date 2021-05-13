n,t=list(map(int,input().split()))
a=list(map(int,input().split()))

dp={}
mina=a[0]
maxdiff=0

for i in range(1,n):
    if a[i]>mina:
        diff=a[i]-mina
        maxdiff=max(maxdiff,diff)

        if diff in dp:
            dp[diff]+=1
        else:
            dp[diff]=1
        
    mina=min(mina,a[i])

print(dp[maxdiff])