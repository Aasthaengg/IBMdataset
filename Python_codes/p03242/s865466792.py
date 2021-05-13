if __name__ == '__main__':
	
	N = input()
	
	s = ""
	for i in N:
		if i == "1":
			s += "9"
		elif i == "9":
			s += "1"
	
	print(s)