def main():
	s = input()

	l = len(s[1 : -1])

	print(s[0] + str(l) + s[-1])

  
if __name__ == "__main__":
  	main()