a, b, c, d = map(int, input().split())

if a==1 or a==9 or a==7 or a==4:
	if b==1 or b==9 or b==7 or b==4:
			if c==1 or c==9 or c==7 or c==4:
					if d==1 or d==9 or d==7 or d==4:
						s = a+b+c+d
						if s==21:
							print('YES')
						else:
							print('NO')
					else:
						print('NO')
			else:
				print('NO')
	else:
		print('NO')
else:
	print('NO')