def solve():
	s = input()
	if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
		return "Bad"
	return "Good"
		
		
if __name__ == "__main__":
	print(solve())