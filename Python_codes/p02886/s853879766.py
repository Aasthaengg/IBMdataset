from itertools import combinations
N = int(input())
d = [int(x) for x in input().split()]

total = 0
for i in list(combinations(d, 2)):
    total += i[0] * i[1]
print(total)
