def rating(n):
	if(n < 600):
		print(8)
	elif(n < 800):
		print(7)
	elif(n < 1000):
		print(6)
	elif(n < 1200):
		print(5)
	elif(n < 1400):
		print(4)
	elif(n < 1600):
		print(3)
	elif(n < 1800):
		print(2)
	elif(n < 2000):
		print(1)
a = int(input())
rating(a)