import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

import numpy as np
N = ri()
A = np.array(ri_())

print(3 ** N - np.prod(np.where(A % 2 == 0, 2, 1)))