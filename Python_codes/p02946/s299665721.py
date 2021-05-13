import numpy as np
k, x = map(int,input().split())
f = max(-1000000, x-k+1)
t = min(1000000, x+k-1)
a = np.arange(f, t+1).tolist()
a = [str(i) for i in a]
print(' '.join(a))
