from itertools import combinations

N = int(input())
d = map(int, input().split())

result = 0
for c in combinations(d, 2):
    result += c[0] * c[1]

print(result)
