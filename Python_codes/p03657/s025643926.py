


import numpy as np
import fractions as fra

a,b=map(int,input().split())
if(a%3!=0 and a%3==b%3):
    print("Impossible")
else:
    print("Possible")