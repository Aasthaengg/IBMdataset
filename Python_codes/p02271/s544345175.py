from itertools import combinations

n, a, q = int(input()), list(map(int, input().split())), input()

l = set(sum(t) for i in range(n) for t in combinations(a, i + 1))

for m in map(int, input().split()):
    print('yes' if m in l else 'no')