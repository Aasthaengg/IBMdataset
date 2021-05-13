n = int(input())
i = 1

while i <= n:
	
	x = i
	
	if x % 3 == 0:
		print(" ", end ="")
		print(i, end ="")
	else:
		while x != 0:
			if x % 10 == 3:
				print(" ", end ="")
				print(i, end ="")
				break
			else:
				x = int(x / 10)
			
	i += 1
print()