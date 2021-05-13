import numpy as np

N, K = map(int, input().split())
h = list(map(int, input().split()))

H = np.array(h)

answer = np.sum(H >= K)

print(answer)
