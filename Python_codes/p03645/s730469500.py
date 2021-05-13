n, m = map(int, input().split())
ikeru = [[] for _ in range(n)]
for i in range(m):
	a, b = map(int, input().split())
	ikeru[a - 1].append(b - 1)
	ikeru[b - 1].append(a - 1)

fukasa = [10 ** 18 for _ in range(n)]
kaisuu = 0
settansaku = set([])
setmada = set([0])
kouho = 1

while kouho != 0:
	kaisuu += 1
	for i in list(setmada):
		settansaku.add(i)
		setmada.remove(i)
		kouho -= 1
		for k in ikeru[i]:
			if not k in setmada:
				if not k in settansaku:
					setmada.add(k)
					kouho += 1
					fukasa[k] = kaisuu

if fukasa[n-1] <= 2:
	print("POSSIBLE")
else:
	print("IMPOSSIBLE")