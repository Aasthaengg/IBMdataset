S = input()
So = S[0::2]
Se = S[1::2]
if 'L' in So:
	print('No')
elif 'R' in Se:
	print('No')
else:
	print('Yes')
