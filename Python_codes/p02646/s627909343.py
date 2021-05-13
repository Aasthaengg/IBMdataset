import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))


A,V=nm()
B,W=nm()
T=int(input())

d=abs(A-B)
move_s=(V-W)
if(move_s<=0):
    print("NO")
    sys.exit(0)
if(((d//move_s))<=(T-1) or ((d//move_s)==T and (d%move_s==0)) ):
    print("YES")
    sys.exit(0)
print("NO")
