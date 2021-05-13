import math
a,b,x = map(int,input().split())

ans = 0

sw = 2*x/(a**3)
sw_c = abs(math.atan(sw))

ans = abs(math.atan(2/a*(b-x/(a**2))))
ans_1 = abs(math.atan(a*b**2/(2*x)))

if(ans < sw_c):
    print(math.degrees(ans))
else:
    print(math.degrees(ans_1))

'''
print("------")
print(math.degrees(ans))
print(math.degrees(sw_c))
print(math.degrees(ans_1))
'''