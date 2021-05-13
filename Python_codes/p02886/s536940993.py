import itertools
N = int(input())
ds = list(map(int, input().split()))
DC = list(itertools.combinations(ds, 2))
L = 0
for i in DC:
	L += i[0]*i[1]
print(L)