import math
N=int(input())

min = N/1.08
max = (N+1)/1.08

candidate = math.ceil(min)
if candidate >= max:
    print(':(')
else:
    print(candidate)