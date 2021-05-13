N,K=map(int, input().split())
sushi=sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1], reverse=True)

typ = set()
ans = 0
cur = 0
rem = []

for t,d in sushi:
	if t in typ:
		if K > 0:
			K -= 1
			cur += d
			rem.append(d)
	else:
		typ.add(t)
		cur += d
		if K > 0:
			K -= 1
		elif len(rem):
			cur -= rem.pop()
		else:
			break

	ans = max(ans, cur + len(typ)**2)

print(ans)
