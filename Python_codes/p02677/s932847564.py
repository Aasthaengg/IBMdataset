import math
A,B,H,M = map(int,input().split())

long = 6.0*M
short = 30.0*H+0.50*M

ans = (A**2+B**2-2*A*B*math.cos(math.radians(long-short)))**0.5
print(ans)
