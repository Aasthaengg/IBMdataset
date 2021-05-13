s=input()
k=int(input())
ans=["zzzzzz"]*k
for i in range(len(s)):
  for j in range(i,min(i+8,len(s))):
    A=s[i:j+1]
    if A>ans[k-1]:
      continue
    if A in ans:
      continue
    for ii in range(k):
      if A<ans[ii]:
        break
    for jj in range(k-1,ii,-1):
      ans[jj]=ans[jj-1]
    ans[ii]=A
print(ans[-1])