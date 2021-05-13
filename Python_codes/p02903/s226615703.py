import numpy as np
H, W, A, B = map(int, input().split())

mat = [np.array(([0] * A) + ([1] * (W - A))) for _ in range(H)]

for i in range(min(H, B)):
    mat[i] = 1 - mat[i]

mat = [r.astype(str).tolist() for r in mat]
print("\n".join("".join(r) for r in mat))