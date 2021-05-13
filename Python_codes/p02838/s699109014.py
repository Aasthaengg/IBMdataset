import os
import sys
import numpy as np

def solve(A, N):
    mod = 10**9+7
    C = [0] * 60
    for a in A:
        for i in range(60):
            if a>>i&1:
                C[i] += 1
    ans = 0
    for i, c in enumerate(C):
        ans += (1<<i) % mod * c % mod * (N-c) % mod
    return ans % mod

# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8[:],i8)"],
]
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
else:
    from numba import njit
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature, cache=True)(func)
    print("compiled!", file=sys.stderr)
# <<< numba compile <<<

N = int(input())
A = np.array(input().split(), dtype=np.int64)
print(solve(A, N))
