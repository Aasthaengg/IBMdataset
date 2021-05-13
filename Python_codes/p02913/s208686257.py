import sys
import numpy as np
from numba import njit

def main(N, S):
    dp = np.zeros((N + 1, N + 1), dtype=np.int64)
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            dp[i,j] = min(j - i, dp[i - 1,j - 1] + 1) if S[i] == S[j] else 0
        ans = max(ans, np.max(dp[i]))
    return ans


if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8,i8[:])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
else:
    from my_module import main
    N = int(input())
    S = np.array([ord(_) for _ in input()])
    print(main(N, S))
