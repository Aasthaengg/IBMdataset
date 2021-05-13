#ABC071A
import math
x, a, b =list(map(int, input().split()))

ax = math.fabs(a-x)
bx = math.fabs(b-x)

if (ax < bx): print("A")
else: print('B')