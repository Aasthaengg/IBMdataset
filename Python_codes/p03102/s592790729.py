import numpy as np

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = np.zeros((N, len(B)))

for n in np.arange(N):
    A[n] = list(map(int, input().split()))

ans = 0
for n in np.arange(N):
    if np.dot(A[n], B) + C > 0:
        ans += 1

print(ans)