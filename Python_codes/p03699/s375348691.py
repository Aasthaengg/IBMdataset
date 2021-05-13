import sys
import copy
import math
import itertools
import numpy as np
import re

N = int(input())
s = [int(input()) for c in range(N)]
ans = sum(s)
s = [c for c in sorted(list(set(s))) if c%10 != 0]

if ans % 10 ==0:
    if len(s) > 0:
        print(ans-s[0])
        sys.exit(0)
    else:
        print(0)
        sys.exit(0)
else:
    print(ans)
    sys.exit(0)

print(0)