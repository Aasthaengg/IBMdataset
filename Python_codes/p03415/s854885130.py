def resolve():
	seq = [input() for _ in range(3)]
	ans = ''
	for i in range(3):
		ans += seq[i][i]
	print(ans)
resolve()