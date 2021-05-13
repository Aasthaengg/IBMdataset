import sys
import math
a,b = map(int,input().split())
if not (1 <= a <= 100 and 1 <= b <= 100):
    sys.exit()

print(math.ceil( (a + b) / 2) )