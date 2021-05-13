def plural():
	s = input()
	if s[-1] == 's' : ans = s + "es"
	else : ans = s + "s"
	return ans

def main()	:
	print(plural())

if __name__	 == '__main__' :
	main()