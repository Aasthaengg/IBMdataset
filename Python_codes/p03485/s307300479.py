import numpy as np
A,B = map(int,input().split())
ans = int(np.ceil((A+B)/2))
print(ans)