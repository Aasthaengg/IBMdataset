from collections import deque
import numpy as np

nCr = {}


def cmb(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = cmb(n-1, r) + cmb(n-1, r-1)
    return nCr[(n, r)]


N, P = map(int, input().split())
A = np.array(list(map(int, input().split())))

li = list(np.mod(A, 2))
zero = li.count(0)
one = li.count(1)

if P == 0:
    combi = [0] + [2 * x for x in range(1, (one + 2) // 2)]
if P == 1:
    combi = [1] + [2 * x + 1 for x in range(1, (one + 1) // 2)]

q = deque(combi)

right = 0
while q:
    c = q.popleft()
    tmp = cmb(one, c)
    right += tmp

print(2**zero * right)