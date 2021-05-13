h,k=list(map(int,input().split()))
def bupdp(l,h,k):
    dp=[0]*(h+1)
    dp[0] = 0
    for i in range(0,h):
        if i>k:
            mini = min([dp[i-j]+abs(l[i]-l[i-j]) for j in range(1,k+1)])             
            dp[i] = mini
        if i<=k and i!=0:
            minim = min([dp[i-j]+abs(l[i]-l[i-j]) for j in range(1,i+1)])
            dp[i] = minim
        if i<1:
            dp[i] = 0
    return dp[-2]

l = list(map(int,input().split()))
print(bupdp(l,h,k))