import math
s = int(input())
h = math.floor(s / 3600)
tmp = s % 3600
m = math.floor(tmp / 60)
s = tmp % 60
a = [h,m,s]
print(":".join(list(map(str, a))))