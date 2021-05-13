import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from itertools import accumulate

N, K = map(int, input().split())

sushi = defaultdict(list)

for i in range(N):
    a,b = map(int, input().split())
    sushi[a].append(b)

first = []
second = []

for nums in sushi.values():
    nums.sort(reverse=True)
    for i, j in enumerate(nums):
        if i == 0:
            first.append(j)
        else:
            second.append(j)
first.sort(reverse=True)
second.sort(reverse=True)

first_cum = [0] + list(accumulate(first))
second_cum = [0] + list(accumulate(second))

ans = 0

for i in range(K, 0, -1):
    neta = min(i, len(first))
    tmp = neta * neta + first_cum[neta]

    if K - neta > len(second):
        break
    
    tmp += second_cum[K - neta]

    ans = max(ans, tmp)

print(ans)