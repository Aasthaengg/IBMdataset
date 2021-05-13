import numpy as np


n = int(input())
a = np.array(list(map(int, input().split())))
a.sort()
a_cum = a.cumsum()
ng = a_cum[:-1] * 2 < a[1:]
ng = np.logical_or.accumulate(ng[::-1])[::-1]
x = (~ng).sum() + 1
print(x)
