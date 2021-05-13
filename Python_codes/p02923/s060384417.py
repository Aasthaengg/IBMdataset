import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
hl = LI()
ans = 0
tmp = 0
for i in range(N-1):
    if hl[i] >= hl[i+1]:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0
print(ans)