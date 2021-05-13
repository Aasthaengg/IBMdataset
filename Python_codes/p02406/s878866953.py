n = int(input())
for i in range(3, n + 1) :
	if(i % 3 == 0 or "3" in str(i)) :
		print(" ", i, sep = "", end = "")
		i += 1
	else :
		pass
print()
