import numpy as np

a,b,c = map(int, input().split())
x = (c-a-b)**2-4*a*b


if(x>0 and c-a-b>=0): print('Yes')
else: print('No')
