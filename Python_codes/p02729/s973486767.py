import math
import itertools

N, M = map(int, input().split())
print(len(list(itertools.combinations(range(N), 2))) + len(list(itertools.combinations(range(M), 2))))