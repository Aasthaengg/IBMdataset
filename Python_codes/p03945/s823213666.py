import numpy as np
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

s = input()
ans = 1
tmp = s[0]
for i in s:
    if i != tmp:
        ans += 1
        tmp = i
print(ans-1)