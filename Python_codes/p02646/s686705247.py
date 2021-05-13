import math
import sys
A,V = map(int, input().split())
B,W = map(int, input().split())
T=int(input())
kyo=abs(A-B)
hay=V-W
if hay<=0 :
    print("NO")
    sys.exit()
if T>=math.ceil(kyo/hay) :
    print("YES")
else:
    print("NO")