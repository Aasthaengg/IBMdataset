from collections import defaultdict
def main():
	H, W, N = map(int, input().split())
	offset = [[i, j] for i in range(-1, 2) for j in range(-1, 2)]
	ans = [0]*10
	ans[0] = (H-2)*(W-2)
	memo = defaultdict(int)
	for i in range(N):
		a, b = map(int, input().split())
		for o in offset:
			if a+o[0] < 2 or H-1 < a+o[0]:
				continue
			if b+o[1] < 2 or W-1 < b+o[1]:
				continue
			memo[(a-1+o[0], b-1+o[1])] += 1
	for v in memo.values():
		ans[v] += 1
		ans[0] -= 1

	for i in range(10):
		print(ans[i])


if __name__ == '__main__':
	main()