N,K=map(int,input().split())
a=[int(i) for i in input().split()]

a.sort()
dp=[0]*(K+1)

for i in range(0,a[0]):
    dp[i]='Second'

for i in range(a[0],K+1):
    for j in a:
        if i<j:
            dp[i]='Second'
            break
        if dp[i-j]=='Second':
            dp[i]='First'
            break
        if j==a[-1]:
            dp[i]='Second'

print(dp[-1])
