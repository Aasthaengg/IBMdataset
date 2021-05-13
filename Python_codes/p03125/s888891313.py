import sys
from collections import Counter
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def IS(): return input()

a, b = MI()
print(a + b) if b % a == 0 else print(b - a)