def calc_sum_of_digits(num):
	ans = 0

	while True:
		if num // 10 == 0:
			ans += num
			break

		ans += num % 10
		num //= 10

	return ans


def main():
	N = int(input())
	min_sum = 1000

	for A in range(1, N):
		B = N - A

		A_sum = calc_sum_of_digits(A)
		B_sum = calc_sum_of_digits(B)

		if A_sum + B_sum < min_sum:
			min_sum = A_sum + B_sum

	print(min_sum)

  
if __name__ == "__main__":
  	main()