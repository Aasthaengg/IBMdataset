import math
A,B,H,M = map(int,input().split())
print((A**2+B**2-2*A*B*math.cos(math.radians((H+M/60)*30-M*6)))**0.5)