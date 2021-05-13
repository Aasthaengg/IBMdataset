import collections
import sys
import math
X=int(input())
if X<100:
    print("0")
    sys.exit()
amari=math.floor(X/100)
kake=amari*5
if amari*100<=X<=amari*100+kake:
    print("1")
else:
    print("0")