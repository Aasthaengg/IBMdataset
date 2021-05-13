from bisect import *
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
data = []
for _ in range(M):
    B, C = map(int, input().split())
    data.append((B, C))
data.sort(key=lambda x:x[1], reverse=True)

D = []
for B, C in data:
    i = bisect_left(A, C)
    p = min(B, i)
    if len(D)+p <N:
        D += [C]*p
    else:
        D += [C]*(N-len(D))
        break

res = 0
for i in range(N):
    if i>=len(D) or A[i] > D[i]:
        res += A[i]
    else:
        res += D[i]
print(res)