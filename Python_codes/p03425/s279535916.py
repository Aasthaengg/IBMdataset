from functools import reduce
from operator import mul
from itertools import combinations
n = int(input())
cnt = [0]*5
for _ in range(n):
    s = input()
    if s[0] not in 'MARCH':
        continue
    i = 'MARCH'.index(s[0])
    cnt[i] += 1


ans = 0
for subset in combinations(range(5), 3):
    ans += reduce(mul, [cnt[i] for i in subset])

print(ans)
