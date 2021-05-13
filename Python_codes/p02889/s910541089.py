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

def solve(N, M, L, ABC, Q, ST):
    inf = 1<<61
    G = np.full((N+1, N+1), inf)
    G.ravel()[::N+2] = 0
    for i in range(M):
        a, b, c = ABC[i]
        G[a, b] = c
        G[b, a] = c
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if G[i, j] > G[i, k] + G[k, j]:
                    G[i, j] = G[i, k] + G[k, j]
    G = np.where(G<=L, 1, inf)
    G.ravel()[::N+2] = 0
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if G[i, j] > G[i, k] + G[k, j]:
                    G[i, j] = G[i, k] + G[k, j]
    G = np.where(G==inf, 0, G) - 1
    #Ans = G[ST[:, 0], ST[:, 1]]
    Ans = np.zeros(Q, dtype=np.int64)
    for i, (s, t) in enumerate(zip(ST[:,0], ST[:,1])):
        Ans[i] = G[s, t]
    return Ans

numba_compile([
    [solve, "i8[:](i8,i8,i8,i8[:,:],i8,i8[:,:])"]
])

N, M, L = map(int, input().split())
ABC = np.array([list(map(int, input().split())) for _ in range(M)], dtype=np.int64)
Q = int(input())
ST = np.array([list(map(int, input().split())) for _ in range(Q)], dtype=np.int64)

Ans = solve(N, M, L, ABC, Q, ST)
print("\n".join(map(str, Ans.tolist())))
