S=input()
T=input()
U=list(S)
V=list(T)
dp=[0]*26
bp=[0]*26
for i in range(len(S)):
  dp[ord(U[i])-97]+=1
  bp[ord(V[i])-97]+=1
dp.sort()
bp.sort()
ans='Yes'
for i in range(len(dp)):
  if dp[i]!=bp[i]:
    ans='No'
    break
print(ans)