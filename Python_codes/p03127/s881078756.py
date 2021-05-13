import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in range(1, n):
        ans = math.gcd(ans, a[i])
    print(ans)
    return 0

if __name__ == "__main__":
    solve()