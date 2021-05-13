import math
h,w,n=[int(input()) for _ in range(3)]
print(math.ceil(n/max(h,w)))