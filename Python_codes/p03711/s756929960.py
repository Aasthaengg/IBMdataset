import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
x, y = M()
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
# c = [2]
if (x in a and y in a) or (x in b and y in b) or x==y:
    print('Yes')
else:
    print('No')