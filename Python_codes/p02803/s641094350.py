import os
import sys
import numpy as np

def solve(H, W, S):
    N = H*W
    G = np.empty((N, N), dtype=np.int64)
    G[:] = 9999999
    for h in range(H):
        for w in range(W):
            i = h*W + w
            G[i, i] = 0
            if w < W-1 and S[h][w] == S[h][w+1] == 46:
                G[i, i+1] = G[i+1, i] = 1
            if h < H-1 and S[h][w] == S[h+1][w] == 46:
                G[i, i+W] = G[i+W, i] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i, j] > G[i, k] + G[k, j]:
                    G[i, j] = G[i, k] + G[k, j]
    # G[G>=9999999] = 0
    G = np.where(G>=9999999, 0, G)

    ans = G.max()
    return ans


# >>> numba compile >>>
numba_config = [
    [solve, "i8(i8,i8,u1[:,:])"],
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


import sys
def main():
    input= sys.stdin.buffer.readline
    H, W = map(int, input().split())
    S = np.array([np.frombuffer(input(), dtype=np.uint8) for _ in range(H)])
    print(solve(H, W, S))

main()
