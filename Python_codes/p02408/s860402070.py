num = int(raw_input())
list_ = [[False for i in range(13)] for j in range(4)]
for x in range(0, num):
	mark, number = map(str, raw_input().split())
	if mark == 'S':
		list_[0][int(number) - 1] = True
	if mark == 'H':
		list_[1][int(number) - 1] = True
	if mark == 'C':
		list_[2][int(number) - 1] = True
	if mark == 'D':
		list_[3][int(number) - 1] = True

for x in range(0, 4):
	for y in range(0, 13):
		if not list_[x][y]:
			if x == 0:
				print "S", y + 1
			elif x == 1:
				print "H", y + 1
			elif x == 2:
				print "C", y + 1
			else:
				print "D", y + 1