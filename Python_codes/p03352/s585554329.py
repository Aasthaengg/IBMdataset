import math
x = int(input())
ans = 0
for b in range(1, int(math.sqrt(x))+1):
    p = 1
    if b != 1:
        while b**p <= x:
            p += 1
    if b**(p-1) > ans:
        ans = b**(p-1)
print(ans)