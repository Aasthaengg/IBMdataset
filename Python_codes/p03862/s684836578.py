import numpy as np
import math
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

n, x = imap()
A = iarr()
ans = 0
for i in range(1, len(A)):
    tmp = A[i] + A[i-1]
    if tmp > x:
        A[i] -= tmp - x
        ans += tmp - x
    A[i] = max(0, A[i])
print(ans)