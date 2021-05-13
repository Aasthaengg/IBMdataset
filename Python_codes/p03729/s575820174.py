

import numpy as np
import math

a=input().split()
for i in range(len(a)-1):
    if(a[i][len(a[i])-1]!=a[i+1][0]):
        print("NO")
        exit(0)
print("YES")