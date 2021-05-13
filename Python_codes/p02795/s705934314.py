h=int(input())
w=int(input())
n=int(input())
ans=0
while n>=1:
  if h>w:
    n-=h
    w-=1
    ans+=1
  else:
    n-=w
    h-=1
    ans+=1
print(ans)