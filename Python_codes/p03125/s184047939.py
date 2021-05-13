import math
inp = input().split()
a = int(inp[0])
b = int(inp[1])

if b/a == math.floor(b/a):
    print(a+b)
else:
    print(b-a)
