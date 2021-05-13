import numpy as np
N = 10**9+7
n = int(input())
a = np.array(input().split(), np.int64)

ans = 0

po = 1
for i in range(61):
    bit = (a>>i) & 1
    s=np.count_nonzero(bit)
    ans+=s*(n-s)%N*po
    ans%=N
    po*=2
    po%=N
print(ans)
