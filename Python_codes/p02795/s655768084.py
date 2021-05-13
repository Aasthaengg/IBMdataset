import math
h = int(input())
w = int(input())
n = int(input())
print(min(math.ceil(n / w), math.ceil(n / h)))