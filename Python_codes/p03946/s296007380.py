import numpy as np
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

n, t = imap()
a = iarr()
b = []
minv = a[0]
for i in a:
    minv = min(i, minv)
    b.append(i - minv)
b.sort(reverse=True)
ans = 0
while b[ans]==b[0]: ans+=1
print(ans)