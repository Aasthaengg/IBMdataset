import sys
from collections import defaultdict
from itertools import accumulate
read = sys.stdin.read

N, K, *A = map(int, read().split())
a = list(accumulate([0] + A))
a = [(a[i] - i) % K for i in range(N + 1)]

answer = 0
dic = defaultdict(int)

for i, x in enumerate(a):
    answer += dic[x]
    dic[x] += 1
    if i >= K - 1:
        dic[a[i - K + 1]] -= 1

print(answer)