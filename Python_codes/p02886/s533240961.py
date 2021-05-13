from itertools import combinations
n = int(input())
d = list(map(int, input().split()))
print(sum(d[i]*d[j] for i, j in combinations(range(n), 2)))