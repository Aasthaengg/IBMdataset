import sys
input = sys.stdin.buffer.readline
from collections import deque


def main():
	n = int(input())

	def label(a, b):
		if a > b:
			a, b = b, a
		return (a - 1) * (2 * n - a) // 2 + b - a - 1

	m = n * (n - 1) // 2
	g = [[] for _ in range(m)]
	deg = [0] * m
	for i in range(1, n + 1):
		l = list(map(int, input().split()))
		for x, y in zip(l, l[1:]):
			t = label(i, y)
			g[label(i, x)].append(t)
			deg[t] += 1

	depth = [None] * m
	q = deque()
	ans = 1
	for i, d in enumerate(deg):
		if not d:
			depth[i] = 1
			q.append(i)
	while q:
		cur = q.popleft()
		for nxt in g[cur]:
			deg[nxt] -= 1
			if not deg[nxt]:
				depth[nxt] = depth[cur] + 1
				if ans < depth[nxt]:
					ans = depth[nxt]
				q.append(nxt)
	print(ans if all(depth) else -1)

if __name__ == "__main__":
	main()