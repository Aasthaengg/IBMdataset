import sys
from collections import defaultdict
import itertools
n = int(input())
dic = defaultdict(lambda : 0)
for _ in range(n):
    s = input()
    if s[0] in 'MARCH':
        dic[s[0]] += 1
if len(dic) <= 2:
    print(0)
    sys.exit()
if len(dic) == 3:
    ans = 1
    for val in dic.values():
        ans *= val
    print(ans)
    sys.exit()

ans = 0
for i, j, k in itertools.combinations(dic.keys(), 3):
    ans += dic[i] * dic[j] * dic[k]
print(ans)