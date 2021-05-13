import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()
ans = ''
xx = int(s[0:2])
zz = int(s[2:4])
if xx < 13 and zz < 13 and xx != 0 and zz != 0:
    ans = 'AMBIGUOUS'
elif xx < 13 and xx != 0:
    ans = 'MMYY'
elif zz < 13 and zz != 0:
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)