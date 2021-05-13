from collections import defaultdict

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
h = defaultdict(int)
g = defaultdict(int)
for k in d:
    h[k] += 1
for k in t:
    g[k] += 1
f = True
for k in g.keys():
    if h[k] < g[k]:
        f = False
        break
print(("YES" if f else "NO"))