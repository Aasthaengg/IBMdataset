from itertools import combinations

def resolve():
	seq = list(map(int, input().split()))
	ans = 0
	cos = []
	comb = combinations(seq, 2)
	for el in comb:
		cos.append(abs(el[0]-el[1]))
	print(sum(cos) - max(cos))
resolve()