#A
N, M = map(int,input().split())
eve=[2*i for i in range(N)]
odd=[2*i+1 for i in range(M)]

from itertools import combinations
comb_eve=len(list(combinations(eve,2)))
comb_odd=len(list(combinations(odd,2)))

print(comb_eve+comb_odd)