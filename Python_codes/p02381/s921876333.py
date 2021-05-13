import math
while True:
	n = input()
	if n==0:break
	s = map(int,raw_input().split(" "))
	m = 0.0
	for i in range(0,n):
		m += s[i]
	a = 0.0
	for i in range(0,n):
		a += (s[i]-m/n)**2
	a = math.sqrt(a/n)
	print a