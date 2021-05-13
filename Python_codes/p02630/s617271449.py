import math
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
from collections import defaultdict
from collections import deque
from collections import Counter
import heapq


def input_li():
    return list(map(int, input().split()))


N = int(input())
A_LI = input_li()
Q = int(input())
cnt = Counter(A_LI)
ans = sum(A_LI)
BC_LI = []
for _ in range(Q):
    BC_LI.append(input_li())
for b, c in BC_LI:
    ans -= b * cnt[b]
    ans += c * cnt[b]
    print(ans)
    if c in cnt:
        cnt[c] += cnt[b]
    else:
        cnt[c] = cnt[b]
    cnt[b] = 0
