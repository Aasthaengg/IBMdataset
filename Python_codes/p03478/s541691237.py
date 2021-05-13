def calc(num, A, B) -> bool:
	ans = 0

	while True:
		if num // 10 == 0:
			ans += num
			break
		ans += num % 10
		num //= 10

	if A <= ans and ans <= B:
		return True
	else:
		return False



def main():
	N, A, B = map(int, input().split())
	ans = 0

	for num in range(1, N + 1):
		result = calc(num, A, B)
		if result:
			ans += num

	print(ans)

  
if __name__ == "__main__":
  	main()