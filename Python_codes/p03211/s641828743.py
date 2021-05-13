
s= raw_input()
m = +float('inf')
for i in range(len(s)):
	if len(s[i:i + 3]) == 3: 
		m = min(abs(int(s[i:i + 3]) - 753), m)
print m