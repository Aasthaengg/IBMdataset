import sys
import math

n, x, t = sys.stdin.readlines()[0].split()
n,x,t = float(n),int(x),int(t)

print(int(math.ceil(n/x) * t))