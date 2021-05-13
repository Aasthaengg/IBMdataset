def main():
	N, C = map(int, input().split())
	sushi_r = [[0 for _ in range(2)] for _ in range(N+2)]
	sushi_l = [[0 for _ in range(2)] for _ in range(N+2)]
	sushi_r[N+1] = [C, 0]
	sushi_l[N+1] = [C, 0]
	dp_r = [0]*(N+2)
	dp_l = [0]*(N+2)
	ans = 0
	for i in range(1, N+1):
		sushi_r[i] = list(map(int, input().split()))
		sushi_r[i][1] += sushi_r[i-1][1]
		dp_r[i] = max(dp_r[i-1], sushi_r[i][1]-sushi_r[i][0])
	for i in range(1, N+1):
		sushi_l[i][0] = C - sushi_r[N-i+1][0]
		sushi_l[i][1] = sushi_r[N-i+1][1]-sushi_r[N-i][1] + sushi_l[i-1][1]
		dp_l[i] = max(dp_l[i-1], sushi_l[i][1]-sushi_l[i][0])

	for i in range(0, N+1):
		ans = max(ans, dp_l[i]-sushi_l[i][0]+dp_r[N-i])
		ans = max(ans, dp_r[i]-sushi_r[i][0]+dp_l[N-i])

	print(ans)


if __name__ == '__main__':
    main()