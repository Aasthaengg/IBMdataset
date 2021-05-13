import sys
import math
x=int(input())
if not ( 1 <= x <= 10**15 ): sys.exit()

print(math.ceil(((x-6)/11)*2)+1)