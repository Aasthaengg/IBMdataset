s = int(input())
import math
k = math.floor(s**0.5)
m = 0
if s == 10**18:
    print(10**9,0,0,10**9,0,0)
else:
    if k**2+k < s:
        m = (k+1)**2 -s
        print(k+1,1,m,k+1,0,0)
    else:
        m = k*(k+1)-s
        print(k+1,1,m,k,0,0)