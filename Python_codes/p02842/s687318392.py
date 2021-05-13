import math


n = int(input())
o = n / 1.080

o_floor = math.floor(o)
o_ceil = math.ceil(o)

if math.floor(o_floor * 1.08) == n:
    print(o_floor)

elif math.floor(o_ceil * 1.08) == n:
    print(o_ceil)

else:
    print(':(')