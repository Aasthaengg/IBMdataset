s = input().rstrip()
n = int(input())
for _ in range(n):
	line = input().rstrip().split()
	a = int(line[1])
	b = int(line[2])
	if line[0] == 'replace':
		p = line[3]
		s = s[0:a] + p + s[b+1:]
	elif line[0] == 'reverse':
		s = s[0:a] + s[a:b+1][::-1] + s[b+1:]
	elif line[0] == 'print':
		print(s[a:b+1])
