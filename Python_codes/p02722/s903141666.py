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

def solve(N):
    if N == 2:
        print(1)
        return
    Ans = [N, N-1]
    for base in range(2, N):
        if base * base > N:
            break
        n = N
        while n % base == 0:
            n //= base
        if n % base == 1:
            Ans.append(base)
        if (N-1) % base == 0:
            Ans.append(base)
            Ans.append((N-1)//base)
    if int(N**0.5)**2 == N:
        Ans.append(int(N**0.5))
    print(len(set(Ans)))

numba_compile([
    [solve, "void(i8)"],
])

N = int(input())
solve(N)
