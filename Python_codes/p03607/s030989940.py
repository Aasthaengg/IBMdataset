from collections import Counter as C

n = int(input())
a = C([input() for _ in range(n)])

print(sum([v % 2 for v in a.values()]))