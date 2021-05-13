
def resolve():
	n = int(input())
	v = []
	for _ in range(n):
		v.append(list(map(int, input().split())))
	t, a = 1, 1
	for i in range(n):
		tv, av = v[i]
		c = max(t//tv + (t%tv!=0), a//av + (a%av!=0))
		t, a = c*tv, c*av
	print(t+a)
resolve()