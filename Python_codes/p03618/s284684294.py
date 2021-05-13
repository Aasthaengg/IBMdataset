from collections import defaultdict
a = input()
n = len(a)
d = defaultdict(int)
ans = n * (n-1) // 2 + 1
for x in a: d[x] += 1
for x in d.values(): ans -= (x) * (x-1) // 2
print(ans)
