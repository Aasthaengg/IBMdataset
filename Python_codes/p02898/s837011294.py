import numpy as np

N, K = map(int, input().split())
H = list(map(int, input().split()))
H = np.array(H) 

print(np.count_nonzero(H >= K))


