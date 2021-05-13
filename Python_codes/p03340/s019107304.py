from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
"""
#N,K,Mが入力
    n,k,m=LI() 
    #N
    #x1 y1
    #.  .
    #xn ynが入力
    N=I()
    p=LIR(N)
    print(n,k,m,p)
"""
from itertools import accumulate

def resolve():
    n=I()
    a=LI()
    asum = list(accumulate(a))
    ans=0
    right=0
    buf=0
    for left in range(n):
        
        
        while right<n and ((asum[right]-asum[left-1] if left>0 else asum[right])==(buf^a[right] if not(left==0 and right==0) else a[right])):
            buf=buf^a[right]
            right+=1
        ans+=right-left
        if left==right:
            right+=1
        else:
            buf=buf^a[left]

    print(ans)

    return
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """4
2 5 4 6"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """9
0 0 0 0 0 0 0 0 0"""
        output = """45"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """19
885 8 1 128 83 32 256 206 639 16 4 128 689 32 8 64 885 969 1"""
        output = """37"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()