#C
import math
from decimal import *
N = int(input())
TA = [list(map(int,input().split())) for i in range(N)]

t,a = 1,1
for i in range(N):
    ti,ai = TA[i]
    n = Decimal(max(math.ceil(t/ti),math.ceil(a/ai)))
    t = n*ti
    a = n*ai
        
    #print(t,a)
    
print(t+a)
