#inport
import sys
import numpy as np
#import itertools as itlt
#from collections import deque

#input 
N,R = [int(x) for x in sys.stdin.readline().split()]

    
if N >= 10:
    ans = R
else:
    ans = R + 100 * (10-N)
        


print(ans)
