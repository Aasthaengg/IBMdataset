N, K = map(int, input().split())
A = list(map(int, input().split()))
import collections
C = collections.Counter(A)
D = sorted(C.items(), key=lambda x: x[1])
B = len(set(A)) -K
result = 0
for a in range(B):
    result += D[a][1]

print(result)