#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
sx,sy,tx,ty=map(int,input().split())
h=ty-sy
w=tx-sx

ans=""
ans+="R"*w+"U"*h
ans+="L"*w+"D"*h
ans+="D"
ans+="R"*(w+1)+"U"*(h+1)+"L"
ans+="U"+"L"*(w+1)+"D"*(h+1)+"R"
print(ans)