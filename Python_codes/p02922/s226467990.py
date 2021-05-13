import math
a, b = map(int, input().split())
up = a-1
gain = b-1
ans = math.ceil(gain/up)
print(ans)