import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

seg_unit = 0


def seg_f(x, y):
    return x | y


def build(seg, raw_data):
    N = len(seg) // 2
    seg[N:] = raw_data
    for i in range(N - 1, 0, -1):
        seg[i] = seg_f(seg[i << 1], seg[i << 1 | 1])


def set_val(seg, i, x):
    N = len(seg) // 2
    i += N
    seg[i] = x
    while i > 1:
        i >>= 1
        seg[i] = seg_f(seg[i << 1], seg[i << 1 | 1])


def fold(seg, l, r):
    vl = vr = 0
    N = len(seg) // 2
    l, r = l + N, r + N
    while l < r:
        if l & 1:
            vl = seg_f(vl, seg[l])
            l += 1
        if r & 1:
            r -= 1
            vr = seg_f(seg[r], vr)
        l, r = l >> 1, r >> 1
    return seg_f(vl, vr)

def main(N, S, query):
    seg = np.zeros(N + N, np.int64)
    build(seg, 1 << S)
    for q in query:
        t, a, b = q.split()
        if t == b'1':
            a, b = int(a) - 1, ord(b) - ord('a')
            set_val(seg, a, 1 << b)
        else:
            a, b = int(a) - 1, int(b)
            x = fold(seg, a, b)
            print(bin(x).count('1'))

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')

    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    seg_f = cc_export(seg_f, (i8, i8))
    build = cc_export(build, (i8[:], i8[:]))
    set_val = cc_export(set_val, (i8[:], i8, i8))
    fold = cc_export(fold, (i8[:], i8, i8))
    cc.compile()

from my_module import seg_f, build, set_val, fold

N = int(readline())
S = np.array(list(readline().rstrip()), np.int64) - ord('a')
query = readlines()[1:]

main(N, S, query)