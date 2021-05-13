def main():
	S = input()
	lst = [False] * 26

	for ch in S:
		lst[ord(ch) - ord("a")] = True

	for i in range(26):
		if lst[i] == False:
			print(chr(i + ord("a")))
			break
	else:
		print("None")

  
if __name__ == "__main__":
  	main()