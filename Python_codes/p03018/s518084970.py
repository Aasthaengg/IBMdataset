s=input()
n=len(s)
ans=0
current=0
flag=0
for i in range(n-1):
  if flag==1:
    flag=0
    continue
  if s[i]=='B' and s[i+1]=='C':
    ans+=current
    flag=1
  elif s[i]=='A':
    current+=1
  else:
    current=0
print(ans)