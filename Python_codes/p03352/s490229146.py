import math
x = int(input())
ans = 0
mx = 0
for b in range(1, int(math.sqrt(x))+1) :
    if b == 1 :
        mx = 1
        continue
    p = 1
    while b ** p <= x :
        mx = max(b**p, mx)
        p += 1
print(mx)
