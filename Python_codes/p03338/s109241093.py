N=int(input())
S=input()
ans=0
for i in range(N+1):
  bns=0
  dp=[0]*26
  bp=[0]*26
  a=S[:i]
  b=S[i:]
  a=sorted(a)
  b=sorted(b)
  for j in range(len(a)):
    dp[ord(a[j])-97]+=1
  for k in range(len(b)):
    bp[ord(b[k])-97]+=1
  for l in range(26):
    if min(dp[l],bp[l])>0:
      bns+=1
  ans=max(ans,bns)
print(ans)