from itertools import combinations

def f(n,x):
	is3 = [sum(c)==x for c in combinations(range(1,n+1),3)]
	return sum(is3)

data = []
while True:
	temp = [int(s) for s in input().split(' ')]
	if temp == [0,0]:
		break
	else:
		data.append(temp)

ans = [f(n,x) for n,x in data]
[print(a) for a in ans]