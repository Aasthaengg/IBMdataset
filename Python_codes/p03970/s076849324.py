s=list(input())
a=list('CODEFESTIVAL2016')
ans=0
for i in range(len(s)):
  if s[i]!=a[i]:
    ans+=1
print(ans)
