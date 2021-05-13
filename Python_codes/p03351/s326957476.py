import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return list(sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

a, b, c, d = LI()
if abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d):
    print('Yes')
else:
    print('No')