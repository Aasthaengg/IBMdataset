'''ABC172 C'''
import numpy as np
n,m,k = map(int,input().split())
a = np.array([int(i) for i in input().split()], dtype='int64')
b = np.array([int(i) for i in input().split()], dtype='int64')

a_c = np.zeros(n+1,dtype='int64')
a_c[1:] = np.cumsum(a)

b_c = np.zeros(m+1,dtype='int64')
b_c[1:] = np.cumsum(b)

a_c = a_c[a_c <= k]
b_c = b_c[b_c <= k]
ans = 0
for i,ai in enumerate(a_c):
    n = np.searchsorted(b_c, k - ai, side = 'right')
    ans = max(i + n-1, ans)
print(ans)