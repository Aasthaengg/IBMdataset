import math
a,b,c= input().split()
x,y,z=(int(a),int(b),int(c))
n = math.floor(y/x)
if n >= z:
    print(z)
else:
    print(n)