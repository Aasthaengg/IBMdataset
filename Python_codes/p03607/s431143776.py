from collections import Counter as C

n = int(input())
a = C([input() for _ in range(n)])

print(sum(map(lambda v:v % 2, a.values())))