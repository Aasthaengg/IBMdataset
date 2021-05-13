k,a,b=map(int,input().split())
ans=1
i=0
while i<k:
  if i==k-1:
    ans=ans+1
    i=i+1
  elif ans<a:
    ans=a
    i=i+a-1
  else:
    if b-a>=2:
      temp=(k-i)//2
      ans=ans+(b-a)*temp
      i=i+2*temp
    else:
      ans=ans+k-i
      i=k
print(ans)
