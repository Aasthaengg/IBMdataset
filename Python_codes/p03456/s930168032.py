import math

a,b = [str(i) for i in input().split()]

num = int(a+b)
sqf_num = math.sqrt(num)
sqi_num = int(sqf_num)

if sqi_num**2 == num:
    print("Yes")
else:
    print("No")