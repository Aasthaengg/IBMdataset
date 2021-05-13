# A The Number of Even Pairs

from itertools import combinations as com

N, M = map(int, input().split())

n = [0] * N
m = [0] * M

ans = len(list(com(n, 2))) + len(list(com(m, 2)))

print(ans)