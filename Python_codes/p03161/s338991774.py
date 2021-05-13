import numba as nb
@nb.njit
def solve(n,k,a):
    dp=[0]*n
    dp[1]=abs(a[1]-a[0])
    for i in range(2,n):
        mi=10**9
        temp=1
        for j in range(i-1,-1,-1):
            if temp>k:
                break
            else:
                temp+=1
            if abs(a[i]-a[j])+dp[j]<mi:
                mi=abs(a[i]-a[j])+dp[j]
        dp[i]=mi
    print(dp[n-1])
n,k=map(int,input().split())
a=list(map(int,input().split()))
solve(n,k,a)