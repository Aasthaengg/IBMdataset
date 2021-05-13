def main():
	N = int(input())
	is_able = False

	for i in range(26):
		for j in range(15):
			if 4 * i + 7 * j == N:
				is_able = True
				break

	if is_able:
		print("Yes")
	else:
		print("No")

  
if __name__ == "__main__":
  	main()