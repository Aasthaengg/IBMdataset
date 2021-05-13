n = int(input())
s = input()
from collections import Counter
c = dict(Counter(s))
ans = 0
for i in c:
    ans *= c[i]+1
    ans += c[i]
print(ans%(10**9+7))