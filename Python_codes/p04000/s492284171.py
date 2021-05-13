# -*- coding: utf-8 -*-
import sys

def main():
	H, W, N = map(int, input().split(" "))
	AB = []
	for _ in range(N):
		a, b = map(int, input().split(" "))
		AB.append((a, b))

	ans = {}
	for i, val in enumerate(AB):
		a, b = val
		a, b = a-1, b-1
		for ba in range(max(0, a-2), min(H-2, a+1)):
			for bb in range(max(0, b-2), min(W-2, b+1)):
				if (ba, bb) in ans.keys():
					ans[(ba, bb)] += 1
				else:
					ans[(ba, bb)] = 1

	ans2 = [0] * 10
	total = (H-2) * (W-2)
	t = 0
	for i in ans.values():
		ans2[i] += 1
		t += 1
	ans2[0] = total - t
	for i in range(10):
		print(ans2[i])

if __name__ == "__main__":
	main()
