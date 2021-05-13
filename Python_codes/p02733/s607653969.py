def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
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

def solve(H, W, K, S):
    ans = 1<<60
    for s in range(1<<H-1):
        an = 0
        f = True
        mapping = np.zeros(H, dtype=np.int64)
        for i in range(H-1):
            if s>>i&1:
                an += 1
                mapping[i+1] = mapping[i]+1
            else:
                mapping[i+1] = mapping[i]
        if an >= ans:
            continue
        Cnt = np.zeros(mapping[-1]+1, dtype=np.int64)
        for x in range(W):
            for y in range(H):
                m = mapping[y]
                c = S[y, x]
                Cnt[m] += c
            if (Cnt > K).any():
                Cnt[:] = 0
                an += 1
                if an >= ans:
                    f = False
                    break
                for y in range(H):
                    m = mapping[y]
                    c = S[y, x]
                    Cnt[m] += c
                if (Cnt > K).any():
                    f = False
                    break
            if not f:
                break
        if f:
            ans = an
    return ans

numba_compile([
    [solve, "i8(i8,i8,i8,i8[:,:])"],
])

def main():
    H, W, K = map(int, input().split())
    S = np.empty((H, W), dtype=np.int64)
    for y in range(H):
        S[y] = np.array(list(input()), dtype=np.int64)
    ans = solve(H, W, K, S)
    print(ans)

main()
