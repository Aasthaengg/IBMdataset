a,b,c = map(int,input().split())
s = a+b+c
if 2*b==s or 2*a==s or 2*c==s:
  print("Yes")
else:
  print("No")