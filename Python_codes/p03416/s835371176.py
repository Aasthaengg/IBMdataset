def checkpalindrome(n):
  s=str(n)
  a=[]
  for i in range(len(s)):
    a.append(s[i])
  a.reverse()
  if ''.join(a)==s:
    return 1
  else:
    return 0
a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
  ans+=checkpalindrome(i)
print(ans)