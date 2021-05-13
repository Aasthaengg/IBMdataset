import math

s = int(input())

rot = int(math.sqrt(s) // 1)
if s == rot**2:
    print("0 0 " + str(rot) + " 0 0 " + str(rot))
    exit()

rot += 1
ans = (rot**2) - s
print("0 0 " + str(rot) + " 1 " + str(ans) + " " + str(rot))
