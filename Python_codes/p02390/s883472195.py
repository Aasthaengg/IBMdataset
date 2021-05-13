import math
S = int(input())
m = (math.floor(S / 60))
h = (math.floor(m / 60))
print(str(h % 60) + ":" + str(m % 60) + ":" + str(S % 60))
