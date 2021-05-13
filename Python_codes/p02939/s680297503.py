s=str(input())
s=list(s)
ans=1
i=1
temp=s[0]
while True:
  if s[i]!=temp:
    ans=ans+1
    temp=s[i]
    i=i+1
  elif s[i]==temp and i==len(s)-1:
    i=i+1
  else:
    temp=s[i]+s[i+1]
    i=i+2
    ans=ans+1
  if i>len(s)-1:
    break
print(ans)