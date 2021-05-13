import sys
from io import StringIO
import unittest

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline

    a,b=map(int, readline().rstrip().split())
    if b%a==0:
        print(a+b)
    else:
        print(b-a)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()