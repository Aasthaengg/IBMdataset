n,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
dp=[[0 for i in range(k+1)] for j in range(2)]
for i in range(k+1):
    for j in range(n):
        if i>=A[j]:
            if dp[1][i-A[j]] is "First":
                dp[0][i]="First"
            if dp[0][i-A[j]] is "Second":
                dp[1][i]="Second"
    if dp[0][i]==0:
        dp[0][i]="Second"
    if dp[1][i]==0:
        dp[1][i]="First"
print(dp[0][-1])
