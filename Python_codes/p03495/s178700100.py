import collections

n, k = map(int,input().split())
a = input().split()
a = sorted(collections.Counter(a).values(), reverse=True)
s = sum(a[:k])

print(0 if s == n else n - s)