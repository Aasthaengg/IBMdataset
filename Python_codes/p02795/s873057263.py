import math
h, w, n = [int(input()) for i in range(3)]
m = 0
ans = math.ceil(n / max(h, w))
print(ans)