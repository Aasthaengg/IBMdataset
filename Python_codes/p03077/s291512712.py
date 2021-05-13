import math

n = int(input())
l = [int(input()) for i in range(5)]

bottle = min(l)

print(math.ceil(n / bottle) + 4)