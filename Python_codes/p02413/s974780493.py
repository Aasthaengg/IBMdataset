r, c = map(int, input().split())
sheet = [[0 for i in range (c)] for j in range(r)]

for i in range(r):
	sheet[i] = input().split()
	k = 0
	for j in range(c):
		k += int(sheet[i][j])
	sheet[i].append(k)
	
l=[0 for i in range (c+1)]
for j in range(c+1):
	for i in range(r):
		l[j] += int(sheet[i][j])
		#print(sheet[i][j])
sheet.append(l)

for i in range(r+1):
	for j in range(c+1):
		if j != c:
			print(sheet[i][j], end=' ')
		else:
			print(sheet[i][j], end='')
			print('')