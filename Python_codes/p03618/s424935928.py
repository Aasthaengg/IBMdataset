import collections
a = list(str(input()))
n = len(a)
c = collections.Counter(a)
result = (n*(n-1))/2 + 1
for i in c.values():
    result -= (i*(i-1))/2
print(int(result))