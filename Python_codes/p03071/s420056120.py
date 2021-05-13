a,b = map(int,input().split())
ans = 0
x = 0
while(x<2):
  if a<b:
    ans+=b
    b-=1
  else:
    ans+=a
    a-=1
  x+=1
print(ans)