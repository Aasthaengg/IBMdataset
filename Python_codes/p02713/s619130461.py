import math
from functools import reduce

k = int(input())

ans = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k+1):
            #ans += reduce(math.gcd, [i, j, l])
            ans += math.gcd(math.gcd(i, j), l)

print(ans)