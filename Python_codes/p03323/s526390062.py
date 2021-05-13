#!/use/bin/env python3

import math
from collections import defaultdict

(a, b) = [int(s) for s in input().split()]

ans = 'Yay!'

if a > 8 or b > 8:
    ans = ':('

print(ans)