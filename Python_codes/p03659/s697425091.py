import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
a_c = a.cumsum()
a_t = a_c[-1]
diff = np.abs(2 * a_c - a_t)
ans = diff[:-1].min()
print(ans)