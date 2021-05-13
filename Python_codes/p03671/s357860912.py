import itertools
m = list(map(int,input().split()))
l = [sum(t) for t in list(itertools.combinations(m, 2))]
print(min(l))