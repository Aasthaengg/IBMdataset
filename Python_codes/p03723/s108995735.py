a, b, c=map(int, input().split())
if a==b and b==c:
  if a%2==1:
    print(0)
  else:
    print(-1)
else:
  cnt=0
  while(1):
    if a%2==1 or b%2==1 or c%2==1:
      print(cnt)
      break
    cnt+=1
    ha=a/2
    hb=b/2
    hc=c/2
    a=hb+hc
    b=ha+hc
    c=ha+hb