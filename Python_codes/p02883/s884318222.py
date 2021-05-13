import sys
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')

    @cc.export('lower_bound', '(i8[:],i8[:],i8,i8,i8)')
    def lower_bound(A, F, ok, ng, k):
        while ok - ng > 1:
            mid = (ok + ng) // 2
            y = A - mid // F
            if y[y > 0].sum() <= k:
                ok = mid
            else:
                ng = mid
        return ok

    cc.compile()
    exit(0)

from my_module import lower_bound
n, k = map(int, input().split())
A = np.array(list(map(int, input().split())))
F = np.array(list(map(int, input().split())))
A = np.sort(A)
F = np.sort(F)[::-1]

ok = 10 ** 16
ng = -1

print(lower_bound(A, F, ok, ng, k))
