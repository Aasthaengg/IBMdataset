A, B, C, D = [int(_) for _ in input().split()]

import numpy as np

# B
b = (B // C + B // D) - (B // np.lcm(C, D))
A = A - 1
a = (A // C + A // D) - (A // np.lcm(C, D))

print(B - A - (b - a))