import numpy as np
N = int(input())
a = np.array(list(map(int,input().split())), dtype=np.int32)
a = np.sort(a)
b = np.diff(a)
c = np.array([2,0]*(N//2), dtype=np.int32)
if N%2==0:
    c = np.array([0] + [2,0]*((N-1)//2), dtype=np.int32)
# print(b,c)
if (b==c).all():
    res = (pow(2, (N-1)//2, 10**9+7) * ((N+1)%2+1)) % (10**9+7)
    print(res)
else:
    print(0)