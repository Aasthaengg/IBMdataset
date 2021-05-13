import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()
n = len(s)
ans = 'Yes'
if s != s[::-1]:
    ans = 'No'
x = math.floor(n/2)
y = math.ceil(n/2)
a = s[0:x]
b = s[y:]
if a != a[::-1] or b != b[::-1]:
    ans = 'No'
print(ans)