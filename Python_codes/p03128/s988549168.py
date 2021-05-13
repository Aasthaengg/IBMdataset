n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
lis = [2,5,5,4,5,6,3,7,6]
def new_val(num1,num2): # 123 , 4 -> 1234
    if num1<0:
        return -(10**10)
    if num1==0:
        return num2
    ret = (10**len(str(num2)))*num1 + num2
    return ret

dp = [[-(10**10) for i in range(1+n)] for j in range(1+m)]
for i in range(m):
    dp[i][0]=0

for i in range(m):
    num=a[i]
    honsu=lis[a[i]-1]
    for j in range(1+n):
        if j<honsu:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(new_val(dp[i+1][j-honsu] , num),dp[i][j])
print(dp[-1][-1])