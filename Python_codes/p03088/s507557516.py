N=int(input())
mod=10**9+7


A=5
dp=[[[[0]*A for _ in range(A)] for _ in range(A)] for _ in range(N+1)]

def check1(a,b,c):
    t=[a,b,c]
    if t==[1,2,4] or t==[1,4,2] or t==[2,1,4]:
        return False
    return True

def check2(a,b,c,m):
    if ([b,c]==[2,4] and m==1) or ([a,c]==[2,4] and m==1):
        return False
    return check1(a,b,c)
    
    
#初期化
for n in range(min(4,N+1)):
    for i in range(A):
        for j in range(A):
            for k in range(A):
                if check1(i,j,k):
                    dp[n][i][j][k]=1
                    
for n in range(4,N+1):
    for i in range(1,A):
        for j in range(1,A):
            for k in range(1,A):
                for m in range(1,A):
                    if check2(i,j,k,m):
                        dp[n][i][j][k]+=dp[n-1][m][i][j]
                dp[n][i][j][k]%=mod
                        
ans=0
if N>=3:
    for i in range(1,A):
            for j in range(1,A):
                for k in range(1,A):
                    ans+=dp[N][i][j][k]

if N==1:
    ans=4
elif N==2:
    ans=16

print(ans%mod)


