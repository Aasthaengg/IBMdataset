import sys
#import numpy as np
import math
from fractions import Fraction
import itertools

input=sys.stdin.readline

a,b,x=map(int,input().split())
ans=b//x-(a-1)//x
print(ans)