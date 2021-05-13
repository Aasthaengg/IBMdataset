from itertools import combinations

N, M = map(int, input().split())

cN = len(list(combinations(range(N),2)))
cM = len(list(combinations(range(M),2)))

print(cN + cM)
