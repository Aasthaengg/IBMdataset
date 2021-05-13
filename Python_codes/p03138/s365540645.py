# coding: utf-8
# Your code here!

N,K=map(int,input().split())

A=list(map(int,input().split()))

cand=[2**i for i in range(40)][::-1]
bit=[0]*40

for a in A:
    for i in range(40):
        if a>=cand[i]:
            a-=cand[i]
            bit[i]+=1

digits=1
while K>=2**(digits):
    digits+=1
#print(digits)
ans=0

if K==0:
    for i in range(40):
        ans+=cand[i]*bit[i]
    print(ans)
    exit()

for i in range(40-digits):
    ans+=cand[i]*bit[i]
#print(ans)


dp=[[[0 for k in range(2)] for j in range(digits)] for i in range(2)]
cand=cand[40-digits:40]
bit=bit[40-digits:40]
dp[0][0][0]=bit[0]*cand[0]
dp[1][0][1]=(N-bit[0])*cand[0]
K-=cand[0]

for i in range(digits-1):
    cor=bit[i+1]*cand[i+1]
    rev=(N-bit[i+1])*cand[i+1]
    if K>=cand[i+1]:
        K-=cand[i+1]
        dp[0][i+1][0]=max(dp[0][i][0],dp[0][i][1],dp[1][i][1],dp[1][i][0])+cor
        dp[0][i+1][1]=max(dp[0][i][0],dp[0][i][1])+rev
        dp[1][i+1][1]=max(dp[1][i][1],dp[1][i][0])+rev
        
    else:#Kに余裕がなくて足せない
        dp[0][i+1][0]=max(dp[0][i][0],dp[0][i][1])+cor
        dp[0][i+1][1]=max(dp[0][i][0],dp[0][i][1])+rev
        dp[1][i+1][0]=max(dp[1][i][0],dp[1][i][1])+cor

#print(dp)

temp=max(max(dp[0][-1]),max(dp[1][-1]))
print(ans+temp)


