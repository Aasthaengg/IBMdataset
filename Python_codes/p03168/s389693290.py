N=int(input())
p=list(map(float,input().split()))
import numpy as np
d=np.zeros(N+2)
d[1]=1
for i in range(N):
    d[1:i+3]=(d[:i+2]*p[i]+d[1:i+3]*(1-p[i]))
print(sum(d[N//2+2:]))