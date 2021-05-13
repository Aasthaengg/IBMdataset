from collections import defaultdict
from itertools import combinations
N = int(input())
dic = defaultdict(list)
for _ in range(N):
    s = input()
    if s[0] in "MARCH":
        dic[s[0]].append(s)

cmb = combinations(dic.keys(),3)
ans = 0
for a,b,c in cmb:
    ans += len(dic[a])*len(dic[b])*len(dic[c])
print(ans)