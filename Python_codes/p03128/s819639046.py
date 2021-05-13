import sys

def get():
	return [int(x) for x in sys.stdin.readline().rstrip().split(" ")]

N, M = get()
A = get()

tukaukazu = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

memo = [0 for x in range(N + 1)]

def search(n):
	if n < 0:
		return None
	else:
		return memo[n]

for n in range(1, N + 1):
	answer = None
	for d in A:
		senzinnnotie = search(n - tukaukazu[d])
		if senzinnnotie is not None:
			candidate = senzinnnotie * 10 + d
			if (answer is None) or (candidate > answer):
				answer = candidate
	memo[n] = answer

print(search(n))
