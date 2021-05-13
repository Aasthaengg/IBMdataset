h=int(input())
hh=h
ans=1
while(1<h):
  h//=2
  ans*=2
  if h==1:
    ans+=ans

if hh==1:
  print(1)
else:
  print(ans-1)


