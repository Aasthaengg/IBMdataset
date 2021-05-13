def main():
    n,t=map(int,input().split())
    F=[tuple(map(int,input().split())) for _ in range(n)]

    dp1=[[0]*t for _ in range(1+n)]
    dp2=[[0]*t for _ in range(1+n)]
    for i in range(n):
        a1=F[i][0]
        b1=F[i][1]
        a2=F[n-i-1][0]
        b2=F[n-i-1][1]
        for j in range(t):
            if j<a1:
                dp1[i+1][j]=dp1[i][j]
            else:
                dp1[i+1][j]=max(dp1[i][j],dp1[i][j-a1]+b1)
            
            if j<a2:
                dp2[i+1][j]=dp2[i][j]
            else:
                dp2[i+1][j]=max(dp2[i][j],dp2[i][j-a2]+b2)
    
    ans=0
    for i in range(n):
        b=F[i][1]
        for j in range(t):
            ans=max(dp1[i][j]+dp2[n-i-1][t-1-j]+b,ans)
    print(ans)          
  
if __name__=='__main__':
    main()