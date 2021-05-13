import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n, k = M()
s = S()
ans = ''
for i in range(1, n+1):
    c = s[i-1]
    if i == k:
        c = c.lower()
    ans += c
print(ans)