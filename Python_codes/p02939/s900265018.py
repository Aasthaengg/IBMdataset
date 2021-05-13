s = list(input())
if len(s) == 1:
    print(1)
    exit()
elif len(s) == 2:
    if s[0] == s[1]:
        print(1)
    else:
        print(2)
    exit()
else:
    dp = [0]*len(s)
    if s[0]==s[1] and s[1]==s[2]:
        dp[0:3]=[1,1,2]
    elif s[0]==s[1] and s[1]!=s[2]:
        dp[0:3]=[1,1,2]
    elif s[0]!=s[1] and s[1]==s[2]:
        dp[0:3]=[1,2,2]
    else:
        dp[0:3]=[1,2,3]

for i in range(3, len(s)):
    if s[i] != s[i-1]:
        dp[i] += dp[i-1]+1
    else:
        dp[i] += dp[i-3]+2

print(dp[-1])