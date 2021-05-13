import collections

n = int(input())
a = [input() for i in range(n)]
b = collections.Counter(a)
print(len(b))