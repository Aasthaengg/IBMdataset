age, b = map(int, input().split())

if age >= 13:
	print(b)
elif 6 <= age < 13:
	print(b // 2)
else:
	print(0)  
