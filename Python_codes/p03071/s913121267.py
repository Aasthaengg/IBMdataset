import math
import sys
a, b = map(int, input().split())
print(max(2*a-1,max(a+b,2*b-1)))