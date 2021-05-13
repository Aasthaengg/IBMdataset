import numpy as np

N, K = map(int, input().split())
p = list(map(int, input().split()))

p = np.array(p)
p = np.sort(p)

ans = p[:K].sum()

print(ans)
