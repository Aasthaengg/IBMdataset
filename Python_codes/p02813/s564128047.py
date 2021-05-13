from itertools import permutations as pu
n = int(input())
p = tuple([int(_) for _ in input().split()])
q = tuple([int(_) for _ in input().split()])
ls = list(pu(range(1, n + 1)))
print(abs(ls.index(p) - ls.index(q)))