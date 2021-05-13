n = int(input())

for a in range(1, 10): 
	b = n // a
	if a * b == n and b >= 1 and b < 10:
		print("Yes")
		quit()

print("No")