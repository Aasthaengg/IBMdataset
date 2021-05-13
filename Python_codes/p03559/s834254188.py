N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))

A.sort()
C.sort()

import bisect

ret = 0
for b in B:
    i = bisect.bisect_left(A, b)
    j = bisect.bisect_right(C, b)

    ret += i * (N - j)
    # print(i, (N - j))

print(ret)

