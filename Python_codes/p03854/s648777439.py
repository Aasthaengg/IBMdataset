s = input()[::-1]
l = [ 'dream', 'dreamer', 'erase', 'eraser']
for i in range(4):
	s1 = l[i][::-1]
	l[i] = s1

n = len(s)
i = 0
t = tuple(l)

while i < n:
	judge = 0
	s_l = []
	for j in (5,6,7):
		if n-i >= j:
			s1 = s[i:i+j]
			if s1 in t:
				i += j
				judge = 1
	
	if judge == 0:
		break

if i == n:
	print('YES')
else:
	print('NO')