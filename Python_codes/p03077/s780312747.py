import math
num = int(input())
min_power = 100000000000000000000000

for i in range(5):
  tmp = int(input())
  if min_power > tmp:
    min_power = tmp

x = math.ceil(num/min_power) + 4
print(x)