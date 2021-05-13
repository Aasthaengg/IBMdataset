import sys
input = sys.stdin.readline

import numpy as np

sw = np.array([int(x) for x in input().split()])
ans = "unsafe" if sw[1] >= sw[0] else "safe"
print(ans)