import math

ds = [int(input()) for _ in range(5)]

d_align = [math.ceil(d / 10) * 10 for d in ds]
d_mirgin = [math.ceil(d / 10) * 10 - d for d in ds]
print(sum(d_align) - max(d_mirgin))