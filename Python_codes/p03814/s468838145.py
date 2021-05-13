def main():
	s = input()

	n = len(s)

	start = -1
	end = n

	for i in range(0, n, 1):
		if s[i] == "A":
			start = i
			break

	for i in range(n - 1, -1, -1):
		if s[i] == "Z":
			end = i
			break
	
	print(end - start + 1)


  
if __name__ == "__main__":
  	main()