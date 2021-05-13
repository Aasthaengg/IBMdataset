import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, b, c = M()
if a[-1] == b[0] and b[-1] == c[0]:
    print('YES')
else:
    print('NO')