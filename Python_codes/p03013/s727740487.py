import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    dp=[0]*(N+1)
    dp[0]=1
    a=[0]*M
    for i in range(M):
        a[i]=I()
        
    a.append(10**6)
    cur=0#aの場所
    
    for i in range(1,N+1):
        if i==a[cur]:
            cur+=1
        else:
            dp[i]=(dp[i-1]+dp[i-2])%mod
            
    print(dp[-1])
    

main()
