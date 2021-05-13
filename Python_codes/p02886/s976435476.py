from itertools import combinations
N = int(input())
D = list(map(int, input().split()))
res = 0
for x, y in combinations(D, 2):
    res += x*y
print(res)