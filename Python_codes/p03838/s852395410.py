import math
import collections
import fractions
import itertools

def solve():
    a, b = map(int, input().split())
    if abs(a) < abs(b):
        ans = abs(b)-abs(a)
        if a < 0:
            ans += 1
        if b < 0:
            ans += 1
        print(ans)
    else:
        ans = abs(a)-abs(b)
        if 0 < a:
            ans += 1
        if 0 < b:
            ans += 1
        print(ans)
    return 0

if __name__ == "__main__":
    solve()
