import collections
l=input().split()

c = collections.Counter(l)

print(len([i[0] for i in c.items() if i[1] >= 1]))