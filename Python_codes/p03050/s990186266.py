import numpy as np
import math

N = int(input())


lim = math.ceil(np.sqrt(N))

ans = 0

for i in range(lim):
    rem = i+1
    if N <= rem**2 + rem:
        break
    if (N-rem) % rem == 0:
        ans += (N-rem)/rem

print(int(ans))
