n,k=map(int,input().split())
a=list(map(int,input().split()))
if k==0:
    ans=0
    for i in a:
        ans+=i^0
    print(ans)
    exit()
l=k.bit_length()-1
dp=[[0,0] for i in range(l+1)]
M=0
for i in a:
    if i>>l&1:
        dp[0][1]+=1<<l
    else:
        dp[0][0]+=1<<l
    M=max(M,i)
p=0
M=M.bit_length()
for i in range(l+1,M):
    for j in a:
        if j>>i&1:
            p+=1<<i
dp[0][0]+=p
dp[0][1]+=p
for i in range(l):
    b=[0,0]
    p=l-i-1
    for j in a:
        if j>>p&1:
            b[0]+=1
        else:
            b[1]+=1
    b[0]<<=p
    b[1]<<=p
    for smaller in range(1,-1,-1):
        if smaller:
            dp[i+1][1]=dp[i][1]+max(b)
        else:
            if k>>p&1:
                dp[i+1][1]=max(dp[i+1][1],dp[i][0]+b[0])
                dp[i+1][0]=dp[i][0]+b[1]
            else:
                dp[i+1][0]=dp[i][0]+b[0]
# print(dp)
print(max(dp[l]))
