def yaya(boo):
  if boo:
    print("Yes")
  else:
    print("No")
a,b,c=map(int,input().split())
yaya(a<=c and c<=b)