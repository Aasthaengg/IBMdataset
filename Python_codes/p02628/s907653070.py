from itertools import product, permutations, combinations
import math
N, K = map(int, input().split())
P = list(sorted((list(map(int, input().split())))))

print(sum([P[i] for i in range(K)]))
exit()
