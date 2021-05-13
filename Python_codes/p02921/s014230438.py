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

    s=readline().rstrip()
    t=readline().rstrip()

    ans=0
    for i in range(3):
        if s[i]==t[i]:
            ans+=1
    print(ans)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------
