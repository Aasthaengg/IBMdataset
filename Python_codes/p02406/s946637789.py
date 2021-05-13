n=int(input())
ans=''
i=1
while(i<=n):
  x=i
  if x%3==0:
    ans+=' '+str(i)
  else:
    while(x>0):
      if x%10==3:
        ans+=' '+str(i)
        break
      x//=10
  i+=1

print(ans)