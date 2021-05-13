import collections
n = int(input())
l = list(input() for i in range(n))
a = collections.Counter(l)
a = list(a.values())
p = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        p += 1
print(p)