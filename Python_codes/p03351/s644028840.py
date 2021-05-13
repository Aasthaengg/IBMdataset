a,c,b,d=map(int,input().split())
a,b=max(a,b),min(a,b)
if (abs(a-c)<=d and abs(c-b)<=d ) or -b+a<=d:print("Yes")
else:print("No")
