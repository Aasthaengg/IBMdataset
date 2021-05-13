import math
L,R,d = map(int, input().split())

minumum = math.ceil(L/d)
maximum = R//d

if maximum - minumum >=0:
    print(maximum - minumum+1)
else:
    print(0)