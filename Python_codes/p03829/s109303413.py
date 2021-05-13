import sys
from io import StringIO
import unittest

doTest=0

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline
    n,a,b=list(map(int, readline().strip().split()))
    xx=list(map(int, readline().strip().split()))
    p=0
    for i in range(1,len(xx)):
        d=xx[i]-xx[i-1]
        p+=min(d*a,b)
    #n,m,k=list(map(int, readline().strip().split()))
    #arr=list(map(int, readline().strip().split()))
    #n=int(readline().strip())
    print(p)

    return

if doTest==0:
    resolve()
    sys.exit()

### ----------------
### ここまでコピぺえ 
### ----------------