def is_palindrome(char) -> bool:
	char_reverse = char[::-1]

	if char == char_reverse:
		return True
	else:
		return False
	

def main():
	A, B = map(int, input().split())
	ans = 0

	for num in range(A, B + 1):
		result = is_palindrome(str(num))

		if result:
			ans += 1

	print(ans)

  
if __name__ == "__main__":
  	main()