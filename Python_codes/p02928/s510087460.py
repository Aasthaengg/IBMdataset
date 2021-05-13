import numpy as np
n,k = map(int,input().split())
a = np.array(list(map(int,input().split())))


af = [0]*n
al = [0]*n

for i in range(n):
    b = a[i+1:]
    af[i] = len(b[b < a[i]])
    al[i] = len(a[a < a[i]])
s = 0

for i in range(n):
    s += al[i] * (k**2 - k*(k+1)//2) + af[i] * k
    s %= 1000000007
print(s)
