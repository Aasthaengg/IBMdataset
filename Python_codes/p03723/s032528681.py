a,b,c=map(int,input().split())
temp=1000
i=0
while i<temp:
  if a%2!=0 or b%2!=0 or c%2!=0:
    print(i)
    break
  else:
    at=a
    bt=b
    ct=c
    a=bt//2+ct//2
    b=at//2+ct//2
    c=at//2+bt//2
    i=i+1
else:
  print(-1)