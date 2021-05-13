import numpy as np

a, b, h, m = map(int, input().split())
rad_a = 2 * np.pi / 720 * (60 * h + m)
rad_b = 2 * np.pi / 60 * m

ans = np.sqrt(a ** 2 + b ** 2 - 2 * a * b * np.cos(rad_a - rad_b))
print("{:.20f}".format(ans))