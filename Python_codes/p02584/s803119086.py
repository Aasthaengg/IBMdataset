x,k,d=map(int,input().split())
x=abs(x)
a=x//d
if a>=k:
  ans=x-(k*d)
else:
  b=x%d
  c=d-b
  if b<=c:
    if (k-a)%2==0:
      ans=b
    else:
      ans=c
  else:
    if (k-a)%2==0:
      ans=b
    else:
      ans=c
print(ans)