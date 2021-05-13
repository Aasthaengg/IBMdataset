n,k = map(int,input().split())
a = list(map(int,input().split()))

c = [0]*50

for i in a:
    for j in range(50):
        if (i >> j) & 1:
            c[j] += 1

s = bin(k)
x = s[2:]


dp = [[0]*2 for i in range(len(x))]
if k != 0:
    dp[0][1] = pow(2,len(x)-1)*(n-c[len(x)-1])
    dp[0][0] = pow(2,len(x)-1)*(c[len(x)-1])
for i in range(1,len(x)):
    dp[i][0] = dp[i-1][0]+pow(2,len(x)-1-i)*max(n-c[len(x)-1-i],c[len(x)-1-i])
    if x[i] == "0":
        dp[i][1] = dp[i-1][1]+pow(2,len(x)-1-i)*c[len(x)-1-i]
    else:
        dp[i][1] = dp[i-1][1]+pow(2,len(x)-1-i)*(n-c[len(x)-1-i])
        dp[i][0] = max(dp[i][0],dp[i-1][1]+pow(2,len(x)-1-i)*(c[len(x)-1-i]))
ans = max(dp[-1])
for i in range(len(x),50):
    if c[i]>0:
        ans += pow(2,i)*c[i]
print(ans)