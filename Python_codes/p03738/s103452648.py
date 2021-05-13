

import numpy as np
import math

a=input()
b=input()

if(len(a)<len(b)):
    print("LESS")
elif(len(a)>len(b)):
    print("GREATER")
elif(a<b):
    print("LESS")
elif(a==b):
    print("EQUAL")
else:
    print("GREATER")
