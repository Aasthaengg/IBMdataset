import sys
import math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
a,b,c = LI()



if c-a-b > 0 and (4*a*b) < ((c-a-b)**2) :
    print('Yes')
else:
    print('No')