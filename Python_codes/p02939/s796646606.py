s=input()
if len(s)<=2:
    print(len(set(list(s))));exit()
dp=[0]*(len(s)+ 1)
dp[0]=0
dp[1]=1
dp[2]=(len(set(list(s[:2]))))

for i in range(3,1+len(s)):
    dp[i]=(dp[i-1]+1) if s[i-1]!=s[i-2]else (dp[i-3]+2)
print(dp[-1])