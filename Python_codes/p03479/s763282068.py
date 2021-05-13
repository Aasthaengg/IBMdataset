import math
x, y = map(int,input().split())

l = 0
while x <= y:
    l += 1
    x = 2*x

print(l)

# なぜWA?
# print(int(math.log2(int(y/x)) + 1))