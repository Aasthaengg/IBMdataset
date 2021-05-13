import numpy as np
a,b,k = map(int,input().split())
c = np.gcd(a,b)
print([i for i in range(1,c+1) if c%i==0][-k])