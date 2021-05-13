n = int(input())

ikeru = [[] for _ in range(n)]
for i in range(n-1):
	a, b, c = map(int, input().split())
	ikeru[a-1].append((b-1, c))
	ikeru[b-1].append((a-1, c))

#fukasa = [0 for _ in range(n)]
#fukasamoto = [0 for _ in range(n)]
kaisuu = 0
settansaku = set([])
setmada = {0}
kouho = 1
guuki = [0 for _ in range(n)]

while kouho != 0:
	kaisuu += 1
	for i in list(setmada):
		settansaku.add(i)
		setmada.remove(i)
		kouho -= 1
		for k, leng in ikeru[i]:
			if not k in setmada:
				if not k in settansaku:
					setmada.add(k)
					guuki[k] = (guuki[i] + leng) % 2
					kouho += 1
					#fukasa[k] = kaisuu
					#fukasamoto[k] = i+1

print("\n".join([str(guuki[i]) for i in range(n)]))