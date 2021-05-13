"""
(sum(j) - sum(i)) % K = j - i
sum(j) % K - sum(i) % K = j- i
j - i < K
"""
n, k = map(int,input().split())
al = list(map(int,input().split()))

import itertools
al_ac = [0] + list(itertools.accumulate(al))

for i in range(n+1):
    al_ac[i] = (al_ac[i] - i) % k

from collections import defaultdict
dic = defaultdict(int)

ans = 0
for i in range(n+1):
    ans += dic[al_ac[i]]
    dic[al_ac[i]] += 1
    if i - k+1 >= 0:
        dic[al_ac[i-k+1]] -= 1

print(ans)
