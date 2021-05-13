N = int(input())
A = list(map(int, input().split()))

import numpy as np
A_np = np.array(A)

ans = 0

while True:
    A_np = A_np / 2
    if len(np.nonzero(A_np%1)[0]) > 0:
        break
    else:
        ans += 1
        
print(ans)