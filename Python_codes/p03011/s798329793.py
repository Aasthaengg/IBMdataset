import itertools
l = list(map(int, input().split()))
p = itertools.permutations(l, 2)
a = [sum(i) for i in p]
print(min(a))