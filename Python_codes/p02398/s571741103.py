import math

inp = raw_input().strip().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
n = 0

for i in range(a,b+1):
    if c%i == 0:
        n += 1

print n