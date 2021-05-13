from math import gcd

from math import factorial as f

from math import ceil, floor, sqrt
import math

import bisect
import re
import heapq

from copy import deepcopy
import itertools
from itertools import permutations

from sys import exit

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

yes = "Yes"
no = "No"


def main():
    n = ii()
    d, x = mi()
    a = []
    for i in range(n):
        tmp = ii()
        a.append(tmp)
    ans = 0
    for i in a:
        tmp = 1
        while tmp <= d:
            ans += 1
            tmp += i
    ans += x
    print(ans)


main()
