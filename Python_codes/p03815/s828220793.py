import math
x = int(input())
tmp = x // 11 * 2

if x%11 == 0:
    tmp += 0
elif x % 11 <= 6:
    tmp += 1
else:
    tmp += 2

print(tmp)
