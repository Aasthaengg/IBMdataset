import collections
import numpy as np
import sys
import copy

W,H,X,Y=map(int,input().split())
#A=list(map(int,input().split()))

if W/2==X and H/2==Y:
    print(X*H,1)


else:
    print(H*W/2,0)