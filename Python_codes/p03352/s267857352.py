import sys
import math
x = int(input())
ans = 0
for i in range(1, x+1):
    for j in range(2, x+2):
        if pow(i, j) <= x:
            ans = max(pow(i, j), ans)
        else:
            break
print(ans)


