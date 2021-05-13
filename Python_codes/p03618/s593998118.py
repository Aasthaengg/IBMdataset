from itertools import accumulate
import math
from collections import deque
from collections import defaultdict
from itertools import permutations
import heapq
import bisect
from collections import Counter
from itertools import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = 10**10
from functools import reduce

A = input()
C = Counter(A)
ans = len(A)*(len(A)-1)//2+1
for k in C.keys():
    ans -= C[k]*(C[k]-1)//2
print(ans)