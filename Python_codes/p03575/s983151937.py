n, m = map(int,input().split())
ikeru = [[] for _ in range(n)]
hashi = []
for i in range(m):
	a, b = map(int, input().split())
	ikeru[a-1].append(b-1)
	ikeru[b-1].append(a-1)
	hashi.append((a-1, b-1))

ans = 0
for num in hashi:
	settansaku = set([])
	setmada = {0}
	kouho = 1
	
	while kouho != 0:
		for i in list(setmada):
			settansaku.add(i)
			setmada.remove(i)
			kouho -= 1
			for k in ikeru[i]:
				if not k in setmada:
					if not k in settansaku:
						if (k, i) != num and (i, k) != num:
							setmada.add(k)
							kouho += 1
	
	if len(settansaku) != n:
		ans += 1

print(ans)