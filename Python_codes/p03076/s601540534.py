a=[int(input()) for _ in range(5)]
import math
b=[math.ceil(i/10)*10-i for i in a]
print(sum(a)+sum(b)-max(b))