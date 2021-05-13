import sys
import numpy as np



def main(N,dp):
    dp[0, 0] = min(N[0], 11 - N[0])
    dp[0, 1] = min(N[0] + 1, 10 - N[0])
    for i in range(1, len(N)):
        dp[i, 0] = min(dp[i - 1, 0] + N[i], dp[i - 1, 1] + 10 - N[i])
        dp[i, 1] = min(dp[i - 1, 0] + N[i] + 1, dp[i - 1, 1] + 9 - N[i])
    print(dp[-1,0])


if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', '(i8[:],i8[:,:])')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
else:
    from my_module import main
    N = np.array([int(_) for _ in input()])
    dp=np.zeros((len(N),2),dtype=np.int64)
    main(N,dp)
