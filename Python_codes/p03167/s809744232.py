def solve(result,rows,cols):
    MOD=10**9+7

    t={"#":1,".":0}
    dp=[[1]*cols for i in range(rows)]
    dp[0][0]=1
    for j in range(1,cols):
        dp[0][j]=dp[0][j-1]*(1-t[result[0][j]])
    for i in range(1,rows):
        dp[i][0]=dp[i-1][0]*(1-t[result[i][0]])
        
    for i in range(1,rows):
        for j in range(1,cols):
            if result[i][j]=="#":
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            
            
    return dp[-1][-1]%MOD

        
    


value=[int(i) for i in input().split()]
rows,cols=value[0],value[1]
result=[]
for i in range(rows):
    t=input()
    result.append(t)
#result=[[str(i) for i in input().split()]for j in range(rows)]
print(solve(result,rows,cols))