from collections import Counter
from collections import defaultdict

S = list(map(str, input().rstrip()))

s = Counter(S)
d = defaultdict(int)

for i in ["a", "b", "c"]:
    d[i] = 0

for l, n in s.items():
    d[l] += n

d = list(d.values())

print("YES" if max(d) - min(d) <= 1 else "NO")