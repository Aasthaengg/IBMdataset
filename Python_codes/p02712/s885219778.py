a=0

for i in range(int(input())+1):
	if i%15==0:
		continue
	elif i%3==0:
		continue
	elif i%5==0:
		continue
	else:
		a+=i
print(a)