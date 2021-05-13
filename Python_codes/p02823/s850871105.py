n,a,b = map(int,input().split())
if (b-a)%2==0:
  print(int((b-a)//2))
else:
  s = a-1
  b1 = b-s
  c = (b1-1)//2+s+1
  
  t = n-b
  a1 = a+t
  d = (n-a1-1)//2+1+t
  print(min(c,d))