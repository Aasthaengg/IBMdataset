a,b,c=map(int,input().split())
ans=0
while a%2==0 and b%2==0 and c%2==0:
  d,e,f=0,0,0
  d=(b+c)//2
  e=(a+c)//2
  f=(a+b)//2
  a,b,c=d,e,f
  ans+=1
  if ans==100000:
    ans=(-1)
    break
print(ans)
