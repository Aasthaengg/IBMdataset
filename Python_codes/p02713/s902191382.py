import math
from functools import reduce

def gcd_list(num_list):
    return reduce(math.gcd, num_list)

K = int(input())

sum = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            sum += gcd_list([a, b, c])

print(sum)