from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

r = list(permutations(range(1, n+1)))
print(abs(r.index(q) - r.index(p)))