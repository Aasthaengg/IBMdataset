import numpy as np

N,M,C = map(int, input().split())
B = np.array(list(map(int, input().split())))
As = [np.array(list(map(int, input().split()))) for _ in range(N)]

ans = 0
for A in As:
    if np.dot(B, A) + C > 0:
        ans += 1
print(ans)