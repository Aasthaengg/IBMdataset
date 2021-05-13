import math
import numpy as np
n = int(input())
li = np.zeros(n, dtype=np.int)
ans = 0
i = 1
while i < n:
    ans += (n-1)//i
    i += 1
print(ans)