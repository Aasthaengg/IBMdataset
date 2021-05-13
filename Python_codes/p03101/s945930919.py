import numpy as np


H, W = map(int, input().split())
h, w = map(int, input().split())
table = np.array([[0 for i in range(W)] for j in range(H)])
ans = 0
for i in range(h):
    table[i] += 1
for i in range(H):
    table[i][:w] += 1
    ans += sum(table[i])
print((H*W)-(ans-(h*w)))
