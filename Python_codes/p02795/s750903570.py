import math
h=int(input())
w=int(input())
n=int(input())
if h>=w: print(math.ceil(n/h))
else: print(math.ceil(n/w))