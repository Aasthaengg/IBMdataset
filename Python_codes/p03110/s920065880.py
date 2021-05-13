import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
J = 0
B = 0
for _ in range(N):
    x, u  = map(str, input().split())
    if u == 'JPY':
        J += int(x)
    else:
        B += float(x)
ans = J + 380000*B
print(ans)