a, b, c = list(map(int, input().split()))
l = [a, b, c]


time_of_exchange = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
	
	if a == b == c:
		time_of_exchange = -1
		break
	
	a = (l[1] + l[2]) / 2
	b = (l[0] + l[2]) / 2
	c = (l[0] + l[1]) / 2
	l = [a, b, c]
	
	time_of_exchange += 1
	
print(time_of_exchange)

