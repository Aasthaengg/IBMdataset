n = int(input())
s = input()

from collections import defaultdict
l = defaultdict(int)
r = defaultdict(int)
for si in s:
    r[si] += 1
r[s[0]] -= 1

ans = l['W'] + r['E']
for i in range(1, n):
    l[s[i-1]] += 1
    r[s[i]] -= 1
    #print(l['W'] , r['E'])
    ans = min(ans, l['W'] + r['E'])
print(ans)
