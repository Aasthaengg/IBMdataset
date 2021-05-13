import math

n = int(input())
a = math.floor(n / 2)
if(n%2 == 0):
    a=a-1

print(a)