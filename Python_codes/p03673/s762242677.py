# ABC 066 C
N = int(input())
A = input().split()
from collections import deque

tmp = deque([])
for i,a in enumerate(A):
    if i %2!=0:
        tmp.appendleft(a)
    else:
        tmp.append(a)
if N%2!=0:
    tmp.reverse()
print(' '.join(tmp))