import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from itertools import accumulate

N, K = map(int, input().split())

sushi = defaultdict(list)

for i in range(N):
    t, d = map(int, input().split())
    sushi[t].append(d)

first = []
second = []
for key in sushi:
    sushi[key].sort(reverse=True)
    first.append(sushi[key][0])
    second += sushi[key][1:]

first.sort(reverse=True)
second.sort(reverse=True)

first_cum = [0] + list(accumulate(first))
second_cum = [0] + list(accumulate(second))


ans = 0
for i in range(1, K+1):
    if K - i <= len(second_cum)-1 and i <= len(first_cum)-1:
        ans = max(ans, first_cum[i] + second_cum[K-i] + i*i)

print(ans)