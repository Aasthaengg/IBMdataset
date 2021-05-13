def varied(s):
	for i in range(1, len(s)):
		if s[i-1] in s[i:]:
			return "no"
	return "yes"

s = input()
print(varied(s))