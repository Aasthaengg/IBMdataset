n = int(input())
d = [int(x) for x in input().split()]
m = int(input())
t = [int(x) for x in input().split()]

from collections import Counter

t = dict(Counter(t))
d = dict(Counter(d))
for i in t.keys():
    if d.get(i)==None or d.get(i)<t.get(i):
        print("NO")
        break
else:
    print("YES")