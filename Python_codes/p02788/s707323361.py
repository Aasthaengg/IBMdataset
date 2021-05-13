def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            vars()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)


import numpy as np

def solve(N, D, A, XH):
    q = []
    idx_q = 0
    I = XH[:, 0].argsort()
    XH = XH[I]
    XH[:, 1] = -(-XH[:, 1]//A)
    d = 0
    ans = 0
    for i in range(N):
        x, h = XH[i]
        while idx_q < len(q) and q[idx_q][0] <= x:
            d -= q[idx_q][1]
            idx_q += 1
        if d < h:
            q.append((x + D*2+1, h-d))
            ans += h-d
            d = h
    return ans

numba_compile([
    [solve, "i8(i8,i8,i8,i8[:,:])"],
])

import sys
def main():
    N, D, A = map(int, input().split())
    XH = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(N, 2)
    ans = solve(N, D, A, XH)
    print(ans)

main()
