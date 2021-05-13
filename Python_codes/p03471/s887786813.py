def main():
	N, Y = map(int, input().split())
	ans_10000 = -1
	ans_5000 = -1
	ans_1000 = -1

	for i in range(N + 1):
		for j in range(N - i + 1):
			k = N - i - j
			total = 10000 * i + 5000 * j + 1000 * k
			if total == Y :
				ans_10000 = i
				ans_5000 = j
				ans_1000 = k
				break				
	print(ans_10000, ans_5000, ans_1000)

  
if __name__ == "__main__":
  	main()