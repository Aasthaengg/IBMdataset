import numpy as np
a = input()
N = int(a)

xy = [map(int, input().split()) for _ in range(N)]
x, y = np.array([list(i) for i in zip(*xy)])

z = x + y
w = x - y

ans = max((max(z)-min(z)),(max(w)-min(w)))
print(ans)