import collections
N = int(input())
l = [str(input()) for i in range(N)]
c = collections.Counter(l)
print(len(c.keys()))