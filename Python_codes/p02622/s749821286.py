s=str(input())
t=str(input())

n=len(s)
num=0
ans=0
while num<n:
  if s[num]!=t[num]:
    ans+=1
  num+=1

print(ans)

