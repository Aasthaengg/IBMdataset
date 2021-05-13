k,a,b=map(int,input().split())
if b-a<=2:
  print(k+1)
else:
  if k<a+1:
    print(k+1)
  else:
    x=(k-a-1)//(2)
    y=k-a-1-x*(2)
    print((b-a)*(x)+b+y)