a, b, c = map(int, input().split())
count = a
num = 0
while count <= b :
	if c % count == 0 :
		num += 1
	count += 1
	if count == b + 1 :
		print(num)