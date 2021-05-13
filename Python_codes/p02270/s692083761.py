def track(A, n, k, P): # 最大積載量Pを決めた時，何個の荷物を載せることができるかを返す
	i = 0
	for _ in range(k):
		weight_of_track_j = 0
		while weight_of_track_j + A[i] <= P:
			weight_of_track_j += A[i]
			i += 1
			if i == n:
				return n
	return i


if __name__ == "__main__":
	n, k = map(int, input().split())
	w = []
	for _ in range(n):
		w.append(int(input()))
	left = 0
	right = 100000 * 10000 # トラックの数 * 荷物の最大重み
	key = n
	while right - left > 1:
		mid = (left + right) // 2
		if key > track(w, n, k, mid):
			left = mid
		else:
			right = mid
	print(right)

