#

import sys
input=sys.stdin.readline

def main():
    MOD=10**9+7
    S=input().strip("\n")
    q=[]
    g=0
    S=S[::-1]
    m13=(1,10,9,12,3,4)
    for i in range(len(S)):
        if S[i] == "?":
            q.append(m13[i%6])
        else:
            x=int(S[i])
            g+=x*m13[i%6]
            g%=13
    if len(q)==0:
        if g==5:
            print(1)
        else:
            print(0)
        exit()
    N=len(q)
    q=[0]+q
    dp=[[0]*13 for i in range(N+1)]
    for j in range(10):
        dp[1][(j*q[1])%13]=1
    for i in range(2,N+1):
        for j in range(13):
            for k in range(10):
                x=(j-k*q[i])%13
                dp[i][j]+=dp[i-1][x]
                dp[i][j]%=MOD
    print(dp[N][(5-g)%13])
    
if __name__=="__main__":
    main()
