import math

n = int(input())
tmp = math.ceil(n/1000)*1000

print(tmp - n)