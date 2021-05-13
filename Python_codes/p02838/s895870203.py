import numpy as np

n = int(input())
a = list(map(int,input().split()))
a = np.array(a,dtype=np.int64)
point = 0
mod = 10**9+7

for i in range(61):
    b = (a >> i)&1
    x = np.count_nonzero(b)
    y = n-x
    point += 2**i*(x*y)%mod

print(point%mod)