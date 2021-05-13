import sys
a,b,c,d=map(int,input().split())
while a>0:
  c-=b
  if c<1:
    print("Yes")
    sys.exit()
  a-=d
print("No")