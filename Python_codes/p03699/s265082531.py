n=int(input())
s=[0]*n
for i in range(n):
  s[i]=int(input())
s.sort()
ans=sum(s)
temp=0
if ans%10==0:
  for i in range(n):
    if s[i]%10==0:
      temp=temp+1
    else:
      print(ans-s[i])
      break
  if temp==n:
    print(0)
else:
  print(ans)