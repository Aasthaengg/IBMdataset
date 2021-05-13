import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
l = []
for v in itertools.permutations(list(range(1, n+1))):
    l.append(v)
l = [0] + l
print(abs(l.index(tuple(p))-l.index(tuple(q))))