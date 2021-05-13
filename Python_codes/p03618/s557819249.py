from collections import defaultdict
A=input()
N=len(A)
dp=[0]*26
x=ord('a')
ans=0
for i in range(N):
    dp[ord(A[i]) - x]+=1
    ans += (i + 1 - dp[ord(A[i]) - x])
    #print(dp,ans)
print(ans+1)
