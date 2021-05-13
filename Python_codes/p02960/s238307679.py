S=input()
S=S[::-1]
dp=[[0]*13 for _ in [0]*(len(S)+1)]
dp[0][0]=1
#dp[n%2][m]:=下位n桁を決定したとき13でわった余りがmになるようなものの数
def pow_k(x,n,p=10**9+7):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=(K*x)%p
        x=(x*x)%p
        n//=2
    return (K*x)%p

p=10**9+7
for n in range(len(S)):
    x=pow_k(10,n,13)
    if S[n]=='?':
        for i in range(10):
            for m in range(13):
                dp[(n+1)][(m+i*x)%13]=(dp[(n+1)][(m+i*x)%13]+dp[n][m])%p
    else:
        s=int(S[n])
        for m in range(13):
            dp[(n+1)][(m+s*x)%13]=dp[n][m]%p

print(dp[len(S)][5]%p)