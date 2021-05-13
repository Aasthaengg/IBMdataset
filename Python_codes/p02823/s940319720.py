n,a,b = map(int,input().split())
x = b-a
if x % 2 == 0 : 
  print(x//2)
else:
  m = (a-1)+1+((b-a-1)//2)
  l = (n-b)+1+((b-a-1)//2)
  print(min(m,l))
