n = int(input())
a = list(map(float,input().split()))
dp = [[0 for i in range(n)] for i in range(n//2+1)]
for i in range((n//2)+1):
    l,j=1,i
    while j<n:
        if i==0:
            l=l*a[j]
            dp[i][j]=l
            j=j+1
        else:
            for k in range(i):
                l=l*(1-a[k])
                dp[i][k]=l
            while j<n:
                dp[i][j]=(dp[i-1][j-1]*(1-a[j]))+(dp[i][j-1]*a[j])
                j=j+1
l=0
for i in range(n//2+1):
    l+=dp[i][n-1]
print(l)
