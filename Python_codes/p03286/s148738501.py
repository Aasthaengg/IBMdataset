n=int(input())

if n==0:
  print(0)
  exit()

ans=''
while n!=0:
  r=n%(-2)
  if r<0:
    r+=2

  ans+=str(r)

  n-=r
  n//=(-2)

print(ans[::-1])