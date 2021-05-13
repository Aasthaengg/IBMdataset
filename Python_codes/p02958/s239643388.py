import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
l = LI()
x = 0
for i in range(1, N+1):
    if i != l[i-1]:
        x += 1
if x > 2:
    print('NO')
else:
    print('YES')