n=int(input())
for i in reversed(range(7)):
	if n>=2**i:
		print(2**i)
		quit()
