N = int(input())
d = list(map(int, input().split()))

import itertools

D = list(range(1, len(d)+1))
p = itertools.permutations(d, 2)

ans = 0
for v in itertools.permutations(D, 2):
    ans = d[v[0]-1] *d[v[1]-1] + ans

print(int(ans/2))