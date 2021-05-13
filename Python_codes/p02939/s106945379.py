s=input()+"--"
n=len(s)-1
ans=0
i=0
a=""
while i<n:
  if s[i]==a:
    i+=1
    a=""
  else:
    a=s[i]
  i+=1
  ans+=1
print(ans-1)