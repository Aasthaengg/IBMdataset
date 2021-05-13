import math
n = int(input())
x = math.ceil(n / 1.08)
print(':(' if int(x * 1.08) != n else x)