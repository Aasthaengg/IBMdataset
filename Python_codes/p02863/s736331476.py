import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,T=map(int,input().split())
    l=[]
    for i in range(N):
        A,B=map(int,input().split())
        l.append((A,B))
    l.sort()
    dp=[[0]*T for _ in range(N)]
    for i in range(N-1):
        for t in range(T-1):
            dp[i+1][t+1]=max(dp[i+1][t+1],dp[i][t+1])
            if t+1>=l[i][0]:
                dp[i+1][t+1]=max(dp[i+1][t+1],dp[i][t+1-l[i][0]]+l[i][1])
    ans=0
    B_sorted=[x[1] for x in l]
    for i in range(1,N):
        ans=max(ans,dp[i][T-1]+max(B_sorted[i:]))
    print(ans)
        

if __name__ == '__main__':
    main()
