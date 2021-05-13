s=input()
ans=""

if len(s)==2:
  print(s)
  
else:
  ans=s[2]
  ans+=s[1]
  ans+=s[0]
  print(ans)