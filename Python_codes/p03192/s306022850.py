num = int(raw_input())
total = 0

while num > 0:
	if num%10 == 2:
		total +=1
	num = num/10

print total