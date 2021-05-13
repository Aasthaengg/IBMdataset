import collections
a,b=map(int,input().split())
n=list(map(int,input().split()))
n=collections.Counter(n)
m,o=zip(*n.most_common())
o=list(o)
print(sum(o)-sum(o[:b]))
