import math 

a,b,c= input().split()
x,y,z=(int(a),int(b),int(c))
p = math.floor(z / x)
print(int(p * y))