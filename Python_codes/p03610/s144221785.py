def main():
	s = input()

	n = len(s)
	ans = ""

	for i in range(0, n, 2):
		ans += s[i]

	print(ans)


  
if __name__ == "__main__":
  	main()