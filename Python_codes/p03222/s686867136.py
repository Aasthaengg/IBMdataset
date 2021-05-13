MOD=10**9+7

def isvalid(bit):
    for t in range(W-2):
        if (bit>>t&1) and (bit>>(t+1)&1):
            return False
    return True

H,W,K=map(int,input().split())
dp=[[0]*W for i in range(H+1)]
dp[0][0]=1

for i in range(1,H+1):
    for k in range(W):
        l,c,r=0,0,0
        for bit in range(2**(W-1)):
            if not isvalid(bit):
                continue
            if ((k>0 and not(bit>>(k-1)&1)) or k==0) and ((k<W-1 and not(bit>>k&1))or k==W-1):
                c+=1
            if (k>0) and (bit>>(k-1)&1):
                l+=1
            if (k<W-1) and (bit>>k&1):
                r+=1
        dp[i][k]=(dp[i][k]+dp[i-1][k]*c)%MOD
        if k>0:
            dp[i][k]=(dp[i][k]+dp[i-1][k-1]*l)%MOD
        if k<W-1:
            dp[i][k]=(dp[i][k]+dp[i-1][k+1]*r)%MOD
print(dp[H][K-1])