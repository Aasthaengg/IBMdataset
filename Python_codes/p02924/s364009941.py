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

    n=int(readline())

    ans=(n * (n-1)) // 2
    
    print(ans)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------