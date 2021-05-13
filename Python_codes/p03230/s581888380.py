from itertools import combinations

N = int(input())
k = 1
while k**2 - k < 2*N: k += 1
if k**2 - k != 2*N: print('No')
else:
    print('Yes')
    print(k)
    sets = [[] for _ in range(k)]
    n = 1
    for i, j in combinations(range(k), 2):
        sets[i].append(n)
        sets[j].append(n)
        n += 1
    for S in sets: print(len(S), *S)