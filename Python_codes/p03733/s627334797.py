import numpy as np
N,T = map(int,input().split())


t = list(map(int,input().split()))

res = T


for i in np.diff(np.array(t)):
    res += min(T,i)

print(res)
