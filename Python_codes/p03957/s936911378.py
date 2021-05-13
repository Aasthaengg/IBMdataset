S = str(input())

if S.count('C') > 0:
	D = S.index('C')
	if S[D::].count('F') > 0:
		print('Yes')
	else:
		print('No')
else:
	print('No')