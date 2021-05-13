import math
n, x, t = map(int, input().split(" "))
 
out = int(math.ceil(n/x)) * t if x != 0 else 0
print(out)