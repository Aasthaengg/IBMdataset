import sys
input = sys.stdin.buffer.readline
from operator import itemgetter as get
from heapq import *


def main():
	n, q = map(int, input().split())
	event = []
	Xs = []
	for _ in range(n):
		s, t, x = map(int, input().split())
		event.append((-2, s - x, x))
		event.append((-1, t - x, x))
		Xs.append(x)
	for _ in range(q):
		d = int(input())
		event.append((0, d, None))
	event.sort(key=get(1))
	active = {x: 0 for x in Xs}
	candidate = []
	ans = []
	for flg, time, x in event:
		if flg == -2:
			active[x] = 1
			heappush(candidate, x)
		elif flg == -1:
			active[x] = 0
		else:
			res = -1
			while candidate:
				c = heappop(candidate)
				if active[c]:
					heappush(candidate, c)
					res = c
					break
			ans.append(res)
	print("\n".join(map(str, ans)))


if __name__ == '__main__':
	main()
