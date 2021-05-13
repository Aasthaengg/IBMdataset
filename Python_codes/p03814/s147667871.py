def main():
	s = input()

	n = len(s)

	start = -1
	end = n

	start = s.index("A")
	end = s.rindex("Z")
	
	print(end - start + 1)


  
if __name__ == "__main__":
  	main()