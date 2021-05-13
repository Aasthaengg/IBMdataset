from itertools import combinations

n = 2019
l, r = map(int, input().split())
if l // n < r // n:
    print(0)
else:
    print(min((i * j) % n for i, j in combinations(range(l % n, r % n + 1), 2)))