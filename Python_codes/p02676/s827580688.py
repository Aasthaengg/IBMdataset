k = int(input())
s = input()

s2 = ""
if len(s) <= k:
	print(s)
else:
	for i in range(k):
		s2 += s[i]
	s2 += "..."
	print(s2)