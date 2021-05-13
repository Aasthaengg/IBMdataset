import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
s = S()
if s == 'SUN':
    print(7)
elif s == 'MON':
    print(6)
elif s == 'TUE':
    print(5)
elif s == 'WED':
    print(4)
elif s == 'THU':
    print(3)
elif s == 'FRI':
    print(2)
elif s == 'SAT':
    print(1)