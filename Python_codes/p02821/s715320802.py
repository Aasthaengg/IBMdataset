import numpy as np

n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
d = 2**18

f = np.zeros(d,dtype=int)
for i in a:
    f[i]+=1

tf = np.fft.rfft(f)
f = np.fft.irfft(tf*tf)
f = [int(i+0.5) for i in f]

ans=0
for i in range(len(f)-1,0,-1):
    if f[i]<=m:
        ans+=i*f[i]
        m-=f[i]
    elif f[i]>m:
        ans+=i*m
        break
print(ans)