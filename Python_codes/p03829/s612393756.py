def main():
	N, A, B = map(int, input().split())
	X = list(map(int, input().split()))
	ans = 0
	for i in range(1, N):
		walk = (X[i]-X[i-1])*A
		if walk < B:
			ans += walk
		else:
			ans += B
	print(ans)

if __name__ == '__main__':
    main()