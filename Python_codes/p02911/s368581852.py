import sys
import numpy as np


def main(stdin):
    N, K, Q = stdin[:3]
    ans = np.full(N + 1, K - Q, dtype=np.int64)
    for i in stdin[3:]:
        ans[i] += 1
    return ans


if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8[:](i8[:],)')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
else:
    #from my_module import main
    stdin = np.array([int(_) for _ in open(0).read().split()])
    ans = main(stdin)
    print(*np.where(ans > 0, 'Yes', 'No')[1:], sep='\n')
