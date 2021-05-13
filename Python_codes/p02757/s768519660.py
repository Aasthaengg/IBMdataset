def main():
	N, P = map(int, input().split())
	S = [int(c) for c in input()]

	if 10 % P == 0:
		ans = 0
		for i in range(N):
			if S[i] % P == 0:
				ans += (i + 1)

		print(ans)
		return


	M = [0] * (N + 1) #左からi番目から最後までの数字のmod p

	t = 1
	for i in range(N - 1, -1, -1):
		M[i] = (M[i + 1] + t % P * S[i]) % P
		t = (t * 10) % P

	C = [0] * 10000

	for v in M:
		C[v] += 1

	ans = 0
	for v in C:
		if v > 0:
			ans += v * (v - 1) // 2

	print(ans)

if __name__ == '__main__':
    main()
