import sys
import numpy as np

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces
sys.setrecursionlimit(10 ** 7)

N = ri()
A = []
B = []

for i in range(N):
    a, b = rl()
    A.append(a)
    B.append(b)

A = np.array(A)
B = np.array(B)
diff = A + B
D = []
for i, x in enumerate(diff):
    D.append((x, i))

D.sort(reverse=True)
A = list(A)
B = list(B)
ta = 0
ao = 0
for x, i in D[::2]:
    ta += A[i]
for x, i in D[1::2]:
    ao += B[i]

print(ta-ao)
