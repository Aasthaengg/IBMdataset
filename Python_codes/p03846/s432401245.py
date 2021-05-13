import sys
import math
in1 = sys.stdin.readlines()
"""
in1 = ['8','7 5 1 1 7 3 5 3']
in1 = ['7','6 4 0 2 4 0 2']
in1 = ['5','2 4 4 0 2']
"""
p = 10 ** 9 + 7
N = int(in1[0])
A_N = list(map(int, in1[1].split()))
A_N.sort()

ckA = []
if N % 2 == 1:
    ckA.append(0)
    oddFlag = 1
else:
    oddFlag = 0

for idx1 in range(1 + oddFlag, N, 2):
    ckA.append(idx1)
    ckA.append(idx1)

if ckA != A_N:
    print(0)
else:
    print((2 ** ((N - oddFlag) // 2)) % p)
