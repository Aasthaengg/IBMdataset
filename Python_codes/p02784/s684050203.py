# 153_b
# B - Common Raccoon vs Monster
import random

H, N = map(int, input().split())
A = input().split()
for i in range(N):
    A[i] = int(A[i])

if (1 <= H, H <= 10 ** 9) and (1 <= N, N <= 10 ** 5):
    for j in range(len(A)):
        H -= A[j]
    if H <= 0:
        print('Yes')
    if H > 0:
        print('No')