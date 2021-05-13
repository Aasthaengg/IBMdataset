import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

x,y = LI()
ans = None

if x == 0:
    ans = abs(y)
    ans += 1 if y<0 else 0
elif x>0:
    if abs(x) == abs(y):
        ans = 1
    elif abs(x) < abs(y):
        ans = abs(y)-abs(x)
        ans += 1 if y<0 else 0
    else:
        ans = 1 + abs(x)-abs(y)
        ans += 1 if y>0 else 0
else:
    if abs(x) == abs(y):
        ans = 1
    elif abs(x) < abs(y):
        ans = 1 + abs(y)-abs(x)
        ans += 1 if y<0 else 0
    else:
        ans = abs(x) - abs(y)
        ans += 1 if y>0 else 0

print(ans)

