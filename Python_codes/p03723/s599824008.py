a,b,c=map(int,input().split())
if a==b and a==c and a%2==0:
  print(-1)
else:
  cnt=0
  while a%2==0 and b%2==0 and c%2==0:
    cnt+=1
    k=a
    l=b
    a=(b+c)//2
    b=(k+c)//2
    c=(k+l)//2
  print(cnt)