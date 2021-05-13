from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

c = Counter(s)
m = max(list(c.values()))
d = sorted(c.items(), key=lambda x: x[1], reverse=True)

t = set()
for i, j in d:
    if j == m:
        t.add(i)
    else:
        break
for i in sorted(t):
    print(i)