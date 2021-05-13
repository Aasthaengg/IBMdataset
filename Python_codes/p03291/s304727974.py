mo=10**9+7
s=input()
n=len(s)
dp=[[0]*(1+n) for i in range(3)]
cc=0
for i in range(n):
    c=s[i]
    if c=='A':
        da,db,dc,dd=1,0,0,1
    elif c=='B':
        da,db,dc,dd=0,1,0,1
    elif c=='C':
        da,db,dc,dd=0,0,1,1
    elif c=='?':
        da,db,dc,dd=1,1,1,3
        
    dp[0][i+1]=dp[0][i]*dd+da*pow(3,cc,mo)
    dp[1][i+1]=dp[1][i]*dd+dp[0][i]*db
    dp[2][i+1]=dp[2][i]*dd+dp[1][i]*dc
    dp[0][i+1]%=mo
    dp[1][i+1]%=mo
    dp[2][i+1]%=mo
    if c=='?':
        cc+=1

print(dp[2][n]%mo)