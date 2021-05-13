h=int(input())

def bupdp(l,h):
    dp=[0]*(h+1)
    dp[0] = 0
    for i in range(0,h):
        if i>1:
            dp[i] = min(dp[i-1]+abs(l[i]-l[i-1]),dp[i-2]+abs(l[i]-l[i-2]))
        if i==1:
            dp[i] = abs(l[i]-l[i-1])
        if i<1:
            dp[i] = 0   
    # print(dp)
    return dp[-2]

l = list(map(int,input().split()))
print(bupdp(l,h))
