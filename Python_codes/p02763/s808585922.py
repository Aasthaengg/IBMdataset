import sys
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


# >>> binary indexed tree >>>
# 必要な要素数+1 の長さの ndarray の 1 要素目以降を使う
def bitify(arr):
    for i in range(1, len(arr)-1):
        arr[i + (i & -i)] += arr[i]
def bit_sum(bit, i):  # [bit_sum, "i8(i8[:],i8)"],
    # (0, i]
    res = 0
    while i:
        res += bit[i]
        i -= i & -i
    return res
def bit_add(bit, i, val):  # [bit_add, "void(i8[:],i8,i8)"],
    n = len(bit)
    while i < n:
        bit[i] += val
        i += i & -i
# <<< binary indexed tree <<<

numba_compile([
    [bitify, "void(i8[:])"],
    [bit_sum, "i8(i8[:],i8)"],
    [bit_add, "void(i8[:],i8,i8)"],
])


def main():
    N = int(sys.stdin.buffer.readline())
    S = np.frombuffer(sys.stdin.buffer.readline()[:-1], dtype=np.uint8).astype(np.int64) - 97
    Q = int(sys.stdin.buffer.readline())
    bits = np.zeros((26, (1<<19)+1), dtype=np.int64)
    bits[S, np.arange(1, N+1)] = 1
    for i in range(26):
        bitify(bits[i])
    Ans = []
    for t, i, c in zip(*[iter(sys.stdin.buffer.read().split())]*3):
        if t == b"1":
            i = int(i)
            c = ord(c)-97
            c_old = S[i-1]
            S[i-1] = c
            bit_add(bits[c_old], i, -1)
            bit_add(bits[c], i, 1)
        else:
            l, r = int(i), int(c)
            ans = 0
            for bit in bits:
                ans += bool(bit_sum(bit, r)-bit_sum(bit, l-1))
            Ans.append(ans)
    print("\n".join(map(str, Ans)))

main()
