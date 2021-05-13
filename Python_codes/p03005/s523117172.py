import sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n,k = Is()
if k == 1 or n == k:
    print(0)
else:
    print(n-k)