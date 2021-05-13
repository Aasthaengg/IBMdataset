s=input()
n=len(s)
dp=[False]*(n+1)
c=["dream","dreamer","erase","eraser"]
if s[:5] in c:
    dp[5]=True
if s[:6] in c:
    dp[6]=True
if s[:7] in c:
    dp[7]=True
for i in range(n+1):
    if dp[i]:
        l=""
        if i+5<=n:
            for idx in range(5):
                l+=s[i+idx]
            if l in c:
                dp[i+5]=True
        if i+6<=n:
            l+=s[i+5]
            if l in c:
                dp[i+6]=True
        if i+7<=n:
            l+=s[i+6]
            if l in c:
                dp[i+7]=True
#print(dp)
if dp[n]:
    print("YES")
else:
    print("NO")