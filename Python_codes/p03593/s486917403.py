# CODE FESTIVAL 2017 qual A
# C - Palindromic Matrix
# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_c
from collections import Counter
import sys
input = sys.stdin.readline
H, W = map(int, input().split())
S = [input()[:-1] for _ in range(H)]
C = Counter(''.join(S))

a = H//2*W//2
b = H//2*(W % 2) + W//2*(H % 2)
c = (H % 2)*(W % 2)

for _ in range(c):
    for k, v in C.items():
        if v % 2 == 1 and v > 0:
            C[k] -= 1
            c -= 1
            break
b += c//2
for _ in range(b):
    for k, v in C.items():
        if v % 4 == 2 and v > 0:
            C[k] -= 2
            b -= 1
            break
a += b//2
for _ in range(a):
    for k, v in C.items():
        if v % 4 == 0 and v > 0:
            C[k] -= 4
            break
if sum(C.values()) == 0:
    print('Yes')
else:
    print('No')
