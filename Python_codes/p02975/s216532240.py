N = int(input())
a = [int(i) for i in input().split()]

from collections import Counter

c = Counter(a)

if c[0] == N:
    print('Yes')
    exit()
if N % 3 != 0:
    print('No')
    exit()
if c[0] == N//3 and len(c) == 2:
    print('Yes')
    exit()
if len(c) != 3:
    print('No')
    exit()
A = list(c.values())
if not (A[0] == N//3 and A[1] == N//3 and A[2] == N//3):
    print('No')
    exit()
B = list(c.keys())
if B[0]^B[1] != B[2]:
    print('No')
    exit()
print('Yes')