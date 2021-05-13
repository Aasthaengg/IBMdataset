from collections import Counter
from itertools import combinations
n = int(input().rstrip())

c = Counter()

for i in range(1,n+1):
    i = str(i)
    a = int(i[0])
    b = int(i[-1])
    c[a, b] += 1

ans = 0
for a, b in combinations(range(1,10), 2):
    ans += 2 * c[a,b] * c[b,a]

for i in range(1,10):
    ans += c[i,i] ** 2

print(ans)