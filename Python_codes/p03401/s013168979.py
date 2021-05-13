def resolve():
	n = int(input())
	seq = [0] + list(map(int, input().split())) + [0]
	v = 0
	for i in range(n+1):
		v += abs(seq[i] - seq[i+1])
	for i in range(1, n+1):
		a = abs(seq[i] - seq[i-1]) + abs(seq[i] - seq[i+1])
		b = abs(seq[i - 1] - seq[i+1])
		print(v - abs(a - b))
resolve()