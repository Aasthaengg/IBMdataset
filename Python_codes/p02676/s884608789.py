if __name__ == '__main__':

	k = int(input())
	s = input()

	ans = ""
	if len(s) > k:
		ans = s[0:k] + "..."
	else:
		ans = s
	print(ans)
