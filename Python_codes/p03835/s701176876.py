def main():
	K, S = map(int, input().split())
	cnt = 0

	for i in range(K + 1):
		for j in range(K + 1):
			k = S - i - j
			if 0 <= k and k <= K:
				cnt += 1

	print(cnt)

  
if __name__ == "__main__":
  	main()