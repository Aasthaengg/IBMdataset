def main():
	N, x = map(int, input().split())
	a = list(map(int, input().split()))

	a.sort()
	a_sum = 0
	ans = 0

	for i in range(N):
		a_sum += a[i]
		ans += 1

		if a_sum > x:
			ans -= 1
			break

		if i == N - 1 and a_sum < x:
			ans -= 1
			break

	print(ans)


  
if __name__ == "__main__":
  	main()