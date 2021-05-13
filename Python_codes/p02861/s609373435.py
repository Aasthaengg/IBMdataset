from itertools import permutations
from collections import defaultdict
import math

def mapt(fn, *args):
    return tuple(map(fn, *args))

n = int(input())
cities = [mapt(int, input().split(" ")) for i in range(n)]
list1 = list(permutations(range(1, n+1), n))


def some(index1, index2):
    index1 -= 1
    index2 -= 1
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    r = math.sqrt((x1-x2)**2 +(y1-y2)**2)
    # print(r)
    return r

ans = 0
for row in list1:
    for i in range(n-1):
        # print(row[i:i+2])
        ans += some(*row[i:i+2])
    # print()
print(ans/len(list1))