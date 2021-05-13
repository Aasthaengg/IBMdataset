# A - AKIBA
substring = ['', 'KIH', 'B', 'R']
akihabara = []

for i in range(16):
	b = format(i, 'b')
	bin_str = b.zfill(4)
	s = ''

	for j in range(4):
		s += substring[j]
		
		if bin_str[j] == '1':
			s += 'A'

	akihabara.append(s)

if input() in akihabara:
	print('YES')
else:
	print('NO')