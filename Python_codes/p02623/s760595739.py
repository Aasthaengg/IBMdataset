from bisect import bisect
from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(1, len(A)):
    A[i] += A[i-1]
for i in range(1, len(B)):
    B[i] += B[i-1]
A.insert(0, 0)
indexB = len(B) - 1
results = [0]
for i in range(len(A)):
    time = A[i]
    if time > K:
        break
    enable_for_b = K - time
    results.append(i + bisect(B, enable_for_b))

print(max(results))