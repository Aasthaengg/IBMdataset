s = input().rstrip()
tmp = 0
pw = 1
from collections import Counter
c = Counter()
c[0] += 1

for d in s[::-1]:
    tmp += int(d) * pw
    tmp %= 2019
    pw *= 10
    pw %= 2019
    c[tmp] += 1

print(sum([v*(v-1)//2 for v in c.values() if v > 1]))