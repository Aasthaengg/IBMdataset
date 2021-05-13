import numpy as np

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

def solve(N, X, Y):
    def bfs(v):
        q = [v]
        Distance = [-1] * (N+1)
        Distance[v] = 0
        distance = 1
        while q:
            q_new = []
            for v in q:
                u = v-1
                if u >= 1 and Distance[u] == -1:
                    Distance[u] = distance
                    q_new.append(u)
                u = v+1
                if u <= N and Distance[u] == -1:
                    Distance[u] = distance
                    q_new.append(u)
                if v == X:
                    u = Y
                    if Distance[u] == -1:
                        Distance[u] = distance
                        q_new.append(u)
                elif v == Y:
                    u = X
                    if Distance[u] == -1:
                        Distance[u] = distance
                        q_new.append(u)
            distance += 1
            q = q_new
        return Distance

    Ans = np.zeros(N, dtype=np.int64)
    for v in range(1, N+1):
        Distance = bfs(v)
        for d in Distance[v+1:]:
            Ans[d] += 1
    return Ans[1:]

numba_compile([
    [solve, "i8[:](i8,i8,i8)"]
])

N, X, Y = map(int, input().split())
Ans = solve(N, X, Y)
print("\n".join(map(str, Ans.tolist())))
