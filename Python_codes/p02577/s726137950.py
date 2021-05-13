import sys
import math

n = str(sys.stdin.readlines()[0])

tot = 0
for dig in n[0:-1]:
    # print(dig)
    tot += int(dig)

if tot % 9 == 0:
    print('Yes')
else:
    print('No')
