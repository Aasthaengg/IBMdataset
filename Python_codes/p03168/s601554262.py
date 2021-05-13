import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    p=list(map(float,input().split()))
    dp=[[float(0)]*(N+1) for _ in range(N+1)]
    dp[0][0]=float(1)
    for i in range(N):
        for omote in range(i+2):
            dp[i+1][omote]+=dp[i][omote]*(1-p[i])
            if omote>=1:
                dp[i+1][omote]+=dp[i][omote-1]*p[i]
    ans=0
    for i in range(-(-(N+1)//2)):
        ans+=dp[N][-(1+i)]
    print(ans)

if __name__ == '__main__':
    main()
