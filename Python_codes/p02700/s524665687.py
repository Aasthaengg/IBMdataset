a,b,c,d = map(int,input().split())

import math

if math.ceil(a / d) >= math.ceil(c / b):
    print("Yes")
else:
    print("No") 
       

