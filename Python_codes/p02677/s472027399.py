A,B,H,M = map(int,input().split())

import math
ans = math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(360*(H/12-M/60+1/60*1/12*M))))



print(ans)