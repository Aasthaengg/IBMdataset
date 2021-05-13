import math
s = input()
s = list(s)

if len(s)%2 == 1:
	l = [0]*(len(s)//2 + 1)
	for i in range(len(s)//2 + 1):
		l[i] = s[2*i]
	L = ''.join(l)
	print(L)
else:
	l = [0]*(len(s)//2)
	for i in range(len(s)//2):
		l[i] = s[2*i]
	L = ''.join(l)
	print(L)