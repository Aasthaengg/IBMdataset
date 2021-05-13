

import numpy as np
import fractions as fra

x,a,b=map(int,input().split())
if(a>=b):
    print("delicious")
elif(a+x>=b):
    print("safe")
else:
    print("dangerous")