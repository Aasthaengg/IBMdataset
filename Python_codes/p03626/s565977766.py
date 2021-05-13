n = int(input())
s = input()
S = input()
dp = [1]*(n+1)
if s[0]== S[0]:ans = 3;i = 1;dp[0] = 1
else:ans = 6;i = 2;dp[1] = 2
while i < n:
    if s[i] == S[i]:
        dp[i] = 1
        if dp[i-1] == 1:ans *= 2
        else: ans *= 1
        i += 1
    else:
        if dp[i-1] == 2:ans *= 3
        else: ans *=2
        dp[i+1]= 2
        i += 2
print(ans%1000000007)