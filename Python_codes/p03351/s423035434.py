a,b,c,d = map(int,input().split())
ab = abs(a-b)
bc = abs(b-c)
ca = abs(c-a)
if ca <= d or  ab<=d and bc<=d:
  print("Yes")
else:
  print("No")