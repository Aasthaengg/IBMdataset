s=input()
n=len(s)
res=0
for i in range(n):
  if s[i]=='A' or s[i]=='C' or s[i]=='G' or s[i]=='T':
    ans=1
    j=i+1
    while j<n:
      if s[j]=='A' or s[j]=='C' or s[j]=='G' or s[j]=='T':
        ans+=1
        j+=1
      else:
        break
  else:
    continue
  res=max(res,ans)
print(res)