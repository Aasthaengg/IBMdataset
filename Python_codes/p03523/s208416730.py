s = input()

flag = [0, 0, 0]

s1 = s
if s1.replace('A', '') == 'KIHBR':
	flag[0] = 1

s2 = s
if 'AA' not in s2:
	flag[1] = 1

s3 = s
if 'KAI' not in s3 and 'IAH' not in s3:
	flag[2] = 1

if flag == [1, 1, 1]:
	print('YES')
else:
	print('NO')