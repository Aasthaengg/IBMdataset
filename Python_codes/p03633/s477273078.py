import numpy as np
n = int(input())
t = [int(input()) for _ in range(n)]

ans = np.lcm.reduce(t)
print(ans)