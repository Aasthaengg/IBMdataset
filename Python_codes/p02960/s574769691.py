

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    N=len(S)
    
    dp=[[0]*13 for _ in range(N+1)]
    dp[0][0]=1
    
    for i in range(N):
        s=S[i]
        
        for j in range(13):
            temp=dp[i][j]
            if s!="?":
                a=int(s)
                nxt=(j*10+a)%13
                dp[i+1][nxt]+=temp
                
            else:
                for k in range(10):# ?=0~9
                    nxt=(j*10+k)%13
                    dp[i+1][nxt]=(dp[i+1][nxt]+temp)%mod
                    
    print(dp[-1][5])
    
    # for i in range(N+1):
    #     print(dp[i])

main()
