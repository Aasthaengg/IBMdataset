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

    s,w=map(int, readline().rstrip().split())
    if w>=s:
        print("unsafe")
    else:
        print("safe")
    #arr=list(map(int, readline().rstrip().split()))
    #n=int(readline())
    #ss=readline().rstrip()
    #yn(1)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------