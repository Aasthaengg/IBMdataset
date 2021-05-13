import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n = I()
k = I()
x = I()
y = I()
ans = 0
for i in range(1, n+1):
    if i<= k:
        ans += x
    else:
        ans += y
print(ans)