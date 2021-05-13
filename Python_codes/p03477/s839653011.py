a,b,c,d=map(int,input().split())
a+=b;c+=d
if a==c:print("Balanced")
if a>c:print("Left")
if c>a:print("Right")