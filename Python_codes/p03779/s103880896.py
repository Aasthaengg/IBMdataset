import numpy as np

x = int(input())

t = np.arange(100000)
ans = np.where(t*(t + 1)//2 >= x)[0][0]

print(ans)