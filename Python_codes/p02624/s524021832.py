import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(N):
    div = np.zeros(N+1, np.int64)
    for n in range(1, N+1):
      for m in range(n, N+1, n):
        div[m] += m
    return div.sum()

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')

    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    main = cc_export(main, (i8, ))
    cc.compile()

from my_module import main

N = int(read())
print(main(N))
