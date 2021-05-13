a,b,c=map(int,input().split())
 
ans = 0
 
while a%2 == b%2 == c%2 == 0:
  ans += 1
  newa=b//2+c//2
  newb=a//2+c//2
  newc=a//2+b//2
  a=newa
  b=newb
  c=newc
  if a == b == c:
    print("-1")
    break
else:
  print(ans)