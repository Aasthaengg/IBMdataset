def check(s, summ):
	for i in s:
		if i % 10 != 0:
			return summ - i
	return 0

t = int(input())
s = []
summ = 0
for _ in range(t):
	n = int(input())
	summ += n
	s.append(n)
s.sort()
if summ % 10 != 0:
	print(summ)
else:
	print(check(s, summ))