a,b,c,d=map(int,input().split())
if abs(a-c)<=d:
  print("Yes")
else:
  print("Yes" if max(abs(a-b),abs(b-c))<=d else "No")