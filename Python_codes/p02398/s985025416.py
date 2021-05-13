a,b,c = map(int,raw_input().split())
num = 1
c_div = []
while num<=c :
	if c%num==0 :
		c_div.append(num)
	num += 1
Count = 0
while a <= b :
	for i in c_div :
		if a==i :
			Count += 1
	a += 1
print '%d' % Count