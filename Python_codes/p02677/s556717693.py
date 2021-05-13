A,B,H,M=map(int,input().split())
kakudo=30*H+M/2-6*M
import math
a=(abs(A**2+B**2-2*A*B*math.cos(math.radians(kakudo))))
answer=a**(1/2)
print(answer)

