s = str(input())
m = 1000
for i in range(len(s) - 2):
	if abs(int(s[i:i+3]) - 753) <=m:
		m = abs( int(s[i:i+3]) -753)
print(m)