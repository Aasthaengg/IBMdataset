from itertools import combinations

N = int(input())
E = [(u, v) for u, v in combinations(range(1, N+1), 2) if u + v != (N//2)*2 + 1]
print(len(E))
for u, v in E: print(u, v)