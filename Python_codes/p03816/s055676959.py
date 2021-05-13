n = int(input())
A = list(map(int, input().split()))

import collections
C = collections.Counter(A)

t = 0
for i in C:
    t += C[i] - 1
if t % 2 == 0:
    print(len(C))
else:
    print(len(C) - 1)