n=input()
ans=0
if int(n)%10==0:
  ans=10
else:
  for i in range(len(n)):
    ans+=int(n[i])
print(ans)