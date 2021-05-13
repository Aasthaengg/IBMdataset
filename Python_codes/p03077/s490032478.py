import math
n=int(input())
a=list(int(input()) for _ in range(5))
print(math.ceil(n/min(a))+4)