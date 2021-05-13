# B - Foods Loved by Everyone
from collections import deque
N,M = map(int,input().split())
K = []
A = []
for o in range(N):
    KA = deque(list(map(int,input().split())))
    Ki = KA.popleft()
    K.append(Ki)
    A.append(list(KA))

common = [0]*(M+1)
for i in A:
    for j in i:
        common[j] += 1
count = 0
for k in common:
    if k == N:
        count += 1
print(count)    