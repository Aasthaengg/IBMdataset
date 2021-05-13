import sys
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')

    @cc.export('is_ok', '(i8[:],i8[:],i8,i8)')
    def is_ok(A, F, x, k):
        y = A - x // F
        tmp = y[y > 0].sum()
        return tmp <= k

    cc.compile()
    exit(0)

from my_module import is_ok
n, k = map(int, input().split())
A = np.array(list(map(int, input().split())))
F = np.array(list(map(int, input().split())))

A = np.sort(A)
F = np.sort(F)[::-1]

ok = 10 ** 16
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(A, F, mid, k):
        ok = mid
    else:
        ng = mid

print(ok)
