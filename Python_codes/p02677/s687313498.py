import numpy as np
A, B, H, M = map(int, input().split())

deg = min(abs(H*360/12 + M*360/12/60 - M*360/60), 360 - abs(H*360/12 + M*360/12/60 - M*360/60))
theta = deg * np.pi /180
ans = np.sqrt(np.power(A,2)+np.power(B,2)-2*A*B*np.cos(theta))
 
print(ans)