from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
C = sorted(C.items(), key=lambda x: x[1])
k = len(C)
c = 0
for i in range(k - K):
    k, v = C[i]
    c += v

print(c)