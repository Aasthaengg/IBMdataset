from sys import stdin

def main():
    
    n=int(stdin.readline().strip())
    a=list(map(int,stdin.readline().strip().split()))
    # dp=[[0,0]*4 for _ in range(n)] #0:<1, 1:-1, 2:1, 3:>1
    # dp[0][0]=[[0,inf][a[0]>=0],[a[0],0][a[0]>=0]]
    # dp[0][1]=[abs(a[0]+1),-1]
    # dp[0][2]=[abs(a[0]-1),1]
    # dp[0][3]=[[0,inf][a[0]<=0],[a[0],0][a[0]<=0]]
    dp=[[[0,0]]*2 for _ in range(n)]
    dp[0][0]=[max(1,a[0])-a[0],[1,a[0]][a[0]>0]]
    dp[0][1]=[a[0]-min(-1,a[0]),[-1,a[0]][a[0]<0]]
    for i in range(1,n):
        n0=[0,1-a[i]-dp[i-1][1][1]][a[i]+dp[i-1][1][1]<=0]
        n1=[0,1+a[i]+dp[i-1][0][1]][a[i]+dp[i-1][0][1]>=0]
        dp[i][0]=[dp[i-1][1][0]+n0,max(1,a[i]+dp[i-1][1][1])]
        dp[i][1]=[dp[i-1][0][0]+n1,min(-1,a[i]+dp[i-1][0][1])]
    print(min(dp[n-1][0][0],dp[n-1][1][0]))

if __name__=='__main__':
    main()
