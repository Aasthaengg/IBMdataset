import numpy as np
a, b, x = map(int, input().split())
if x <= a**2*b/2:
    print(np.rad2deg(np.arctan(b/(2*x/a/b))))
else:
    y = b - x/(a**2)
    print(np.rad2deg(np.arctan(2*y/a)))