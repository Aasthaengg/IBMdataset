import math
K = int(input())
A = [int(_) for _ in input().split()]
l = r = 2
'''
if x children form groups consisting of y children each
 then z children are left
=> z=y*(x//y)
=> y*(math.ceil(z/y))<=x<y*(math.floor(z/y)+1)
'''
#necessary conditions
for a in A[::-1]:
    l = a * math.ceil(l / a)
    r = a * (math.floor(r / a) + 1) - 1
#sufficient conditions
for x in [l, r]:
    for a in A:
        x = a * (x // a)
    if x != 2:
        print(-1)
        exit()
print(l, r)
