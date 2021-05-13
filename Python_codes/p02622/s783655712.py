s=input()
n=input()
a=len(s)
ans=0
for m in range(a):
  if s[m]!=n[m]:
    ans=ans+1
print(ans)