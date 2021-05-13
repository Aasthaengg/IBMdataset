import math
a,b=map(int,input().split())
l=len(str(b))
n=a*(10**l)+b
n1=math.sqrt(n)
if n1==math.floor(n1):
    print("Yes")
else:
    print("No")