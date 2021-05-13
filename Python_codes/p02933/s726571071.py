### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline

    #a,b,c=map(int, readline().rstrip().split())
    #arr=list(map(int, readline().rstrip().split()))
    a=int(readline())
    ss=readline().rstrip()
    if a<3200:
        ss="red"
    print(ss)
    #yn(1)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------