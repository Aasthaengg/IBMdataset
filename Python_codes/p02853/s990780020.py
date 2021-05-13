import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
l = LI()
ans = 0
for i in l:
    if i == 1:
        ans += 300000
    elif i == 2:
        ans += 200000
    elif i == 3:
        ans += 100000
if l[0] == l[1] == 1:
    ans += 400000
print(ans)