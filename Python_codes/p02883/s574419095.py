import sys
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')
    @cc.export('is_ok', '(i8[:],u8[:],u8,u8)')
    
    def is_ok(A, F, x, k):
        y = A - x // F
        tmp = y[y > 0].sum()
        return tmp <= k
      
    cc.compile()
    exit()
from my_module import is_ok

n, k = map(int, input().split())
A = np.array(input().split(), dtype="i8")
F = np.array(input().split(), dtype="u8")

A = np.sort(A)
F = np.sort(F)[::-1]

ok = 10 ** 12
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(A, F, mid, k):
        ok = mid
    else:
        ng = mid

print(ok)

