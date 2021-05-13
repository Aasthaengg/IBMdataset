import sys
import collections
import copy
import math
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
a = int(input())
ans = 0
for i in range(4):
    if a%10 == 2:
        ans += 1
    a = a//10
print(ans)
