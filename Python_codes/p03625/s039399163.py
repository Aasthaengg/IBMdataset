n = int(input())

A = list(map(int, input().split()))

import collections

C = collections.Counter(A)

D = sorted(list(set(A)))[::-1]

t = 0
s = 0
for i in D:
    if C[i] >= 4 and t == 0:
        print(i ** 2)
        s = 1
        break
    elif C[i] >= 2 and t == 0:
        t = i
    elif C[i] >= 2 and t != 0:
        print(i * t)
        s = 1
        break

if s == 0:
    print(0)