x=int(input())

dp=[0]*101000

dp[100]=1
dp[101]=1
dp[102]=1
dp[103]=1
dp[104]=1
dp[105]=1

for i in range(100000):
    if dp[i]!=0:
        dp[i+100]+=1
        dp[i+101]+=1
        dp[i+102]+=1
        dp[i+103]+=1
        dp[i+104]+=1
        dp[i+105]+=1

if dp[x]!=0:
    print("1")

else:
    print("0")

