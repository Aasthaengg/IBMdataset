import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
ans = 0
for i in range(N, 1000):
    s = str(i)
    if s[0] == s[1] == s[2]:
        ans = i
        break
print(ans)