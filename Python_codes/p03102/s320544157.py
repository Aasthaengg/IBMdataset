import numpy as np

N,M,C = map(int, input().split())
B = np.array(input().split(), int)
As = np.array([input().split() for _ in range(N)], int)

ans = 0
for A in As:
    if np.dot(B, A) + C > 0:
        ans += 1
print(ans)