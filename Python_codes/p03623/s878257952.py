import numpy as np

x, a, b = map(int, input().split())
ans = 'A' if np.abs(a-x) < np.abs(b-x) else 'B'
print(ans)