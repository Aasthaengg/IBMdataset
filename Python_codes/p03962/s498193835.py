import collections as c
a = list(map(int, input().split()))
p = c.Counter(a)
print(len(p))