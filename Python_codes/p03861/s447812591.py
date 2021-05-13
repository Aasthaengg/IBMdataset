a,b,x=map(int,input().split())

ap=a//x
bp=b//x

ans=bp-ap
if a%x==0:
  ans+=1

print(ans)