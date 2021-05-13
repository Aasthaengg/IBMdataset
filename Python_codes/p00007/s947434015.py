import sys
import math

for line in sys.stdin:
    n = int(line)
    x = 100000
    y = 0
    for i in range(n):
        x += math.ceil(x*0.05/1000)*1000
    print(x)
    break