N, M = list(map(int, input().split()))
AC = set()
WA = {}

for _ in range(M):
	p, S = input().split()
	p = int(p)
	if S == 'AC':
		AC.add(p)
	else:
		if p not in AC:
			if p in WA:
				WA[p] += 1
			else:
				WA[p] = 1
wa = 0
for k, v in WA.items():
	if k in AC:
		wa += v

print(len(AC), wa)