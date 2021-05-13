import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

n, m, d = map(int, input().split())
if d == 0:
    ans = (m - 1) / n
else:
    ans = 2 * (n - d) * (m - 1) / (n * n)
print(ans)
