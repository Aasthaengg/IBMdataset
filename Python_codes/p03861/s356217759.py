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

a, b, x = imap()
ans = (b//x) - (a//x)
if a % x == 0: ans += 1
print(ans)