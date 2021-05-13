from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import sys
from fractions import gcd
from itertools import count

for line in sys.stdin:
    small, large = sorted(int(n) for n in line .split())
    for i in count(large, large):
        if not i % small:
            lcm = i
            break
    print(gcd(large, small), lcm)